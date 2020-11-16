import python_ibft as ibft
from python_ibft.bls_threshold import reconstruct
from python_ibft import server as ibft_server

import grpc
from concurrent import futures
import time
from queue import Queue
from collections import defaultdict
from copy import deepcopy
from apscheduler.schedulers.background import BackgroundScheduler
from google.protobuf.empty_pb2 import Empty
from datetime import datetime
import json
import base64

# import the generated classes
from .rpc import ssv_pb2
from .rpc import ssv_pb2_grpc
from .rpc import validator_pb2_grpc
from .rpc import validator_pb2
from .rpc import attestation_pb2



# Eth2 slot time logic
SECONDS_PER_SLOT = 12
ATTESTATION_DELAY = SECONDS_PER_SLOT // 3


# Global state variables
streaming_event_queues = []
# Partial signature store until enough available for reconstruction
partial_attestation_store = defaultdict(dict)
# Store the attestation data
# TODO: Replace this by loading attestation data from serialized attestation, so also nodes that didn't
# get the attestation data can sign after commit quorum reached
attestation_data_store = {}


def get_current_slot():
    return (time.time() - genesis_time) // SECONDS_PER_SLOT

def get_slot_time(slot):
    return slot * SECONDS_PER_SLOT + genesis_time



def get_attestation_and_sign(slot, committee_index):
    request = validator_pb2.AttestationDataRequest(slot=slot, committee_index=committee_index)
    response = stub.GetAttestationData(request)
    attestation = response
    ibft.start_instance(attestation.target.epoch, base64.encodebytes(attestation.SerializeToString()).decode("utf-8"), decision_callback=decision_callback)


def decision_callback(serialized_attestation):
    attestation = attestation_pb2.AttestationData()
    attestation.ParseFromString(base64.decodebytes(serialized_attestation.encode("utf-8"))) #.decode("iso8859_15")
    for request, stream in streaming_event_queues:
        task = ssv_pb2.SSVTask(public_key=threshold_public_keys[process_id],
                        topic=ssv_pb2.SIGN_ATTESTATION,
                        attestation=attestation)
        stream.put(task)


# Broadcast callback -- this is called by the IBFT library when a partial signature is broadcast
# Need to aggregate and reconstruct if we have more than the threshold
def broadcast_callback(msg, sender):
    if msg["type"] == "signed_attestation":
        print("Received signed attestation from process_id={0}".format(sender))
        partial_attestation_store[msg["attestation"]][sender] = bytes.fromhex(msg["signature"])

        if len(partial_attestation_store[msg["attestation"]]) == 3:
            print("Got 3 attestation signatures, ready to reconstruct")
            store = deepcopy(partial_attestation_store[msg["attestation"]])
            full_signature = reconstruct(store)
            attestation = attestation_data_store[msg["attestation"]]
            attestation.signature = full_signature

            x = stub.ProposeAttestation(attestation)
            print(x)



# GRPC Server that implements the SSV streaming endpoint (sends attestations for VC to sign)
class SSVServicer(ssv_pb2_grpc.SSVServicer):

    def GetTaskStream(self, request, context):
        print("Validator node connected")
        stream = Queue()
        streaming_event_queues.append((request, stream))
        while True:
            response = stream.get()
            yield response


# GRPC server that implements pass-through endpoints to the beacon node
class BeaconProxy(validator_pb2_grpc.BeaconNodeValidatorServicer):

    def DomainData(self, request, context):
        return stub.DomainData(request)


    def ProposeAttestation(self, request, context):
        serialized = base64.encodebytes(request.data.SerializeToString()).decode("utf-8")

        attestation_data_store[serialized] = deepcopy(request)

        ibft.send_broadcast({"type": "signed_attestation", "attestation": serialized, "signature": request.signature.hex()})

        return validator_pb2.AttestResponse(attestation_data_root=bytes.fromhex("c797a8d3aa7c4174a0bf84f4ef3a06c3f9fe8e998fbb8374ae31ad8d003b5955"))

    def GetDuties(self, request, context):
        request.public_keys[0] = public_key
        duties = stub.GetDuties(request)
        return duties



def init(beacon_rpc, pid, ibft_parties, ibft_config, privkey_json, pubkey, threshold_pubkeys, rpc_port):

    global process_id, public_key, threshold_public_keys, channel, stub, genesis_time

    process_id = pid
    public_key = pubkey
    threshold_public_keys = threshold_pubkeys

    # open a gRPC channel to the beacon node
    channel = grpc.insecure_channel(beacon_rpc)


    # Setup IBFT

    # Broadcast function
    ibft.broadcast_callback = broadcast_callback

    # Start IBFT service
    ibft_server.start_ibft(privkey_json, ibft_parties, ibft_config, process_id)


    # Start scheduler
    scheduler = BackgroundScheduler()
    scheduler.start()

    # Start GRPC service
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    ssv_pb2_grpc.add_SSVServicer_to_server(
            SSVServicer(), server)
    validator_pb2_grpc.add_BeaconNodeValidatorServicer_to_server(BeaconProxy(), server)
    print('Starting server. Listening on port {0}.'.format(rpc_port))
    server.add_insecure_port('[::]:{0}'.format(rpc_port))
    server.start()

    stub = validator_pb2_grpc.BeaconNodeValidatorStub(channel)
    syncedResponse = stub.WaitForSynced(Empty()).next()
    genesis_time = syncedResponse.genesis_time

    # create a request for the duties streaming endpoint
    request = validator_pb2.DutiesRequest(epoch=1, public_keys=[public_key])

    # make the call
    response = stub.StreamDuties(request)

    # Loop that gets new duties and schedules an IBFT process to decide on them
    for new_duty in response:
        # Compute time of the slot to attest
        attestation_time = get_slot_time(new_duty.current_epoch_duties[0].attester_slot)
        print(datetime.fromtimestamp(attestation_time).isoformat())

        # Subscribe to the right subnets to broadcast attestations
        ssr = validator_pb2.CommitteeSubnetsSubscribeRequest(
                slots=[new_duty.current_epoch_duties[0].attester_slot, 
                        new_duty.next_epoch_duties[0].attester_slot], 
                        committee_ids=[new_duty.current_epoch_duties[0].committee_index,
                        new_duty.next_epoch_duties[0].committee_index], 
                        is_aggregator=[False, False])

        stub.SubscribeCommitteeSubnets(ssr)

        scheduler.add_job(lambda: get_attestation_and_sign(
                        new_duty.duties[0].attester_slot,
                        new_duty.duties[0].committee_index
                ),
                trigger="date",
                run_date=datetime.fromtimestamp(attestation_time + ATTESTATION_DELAY))
