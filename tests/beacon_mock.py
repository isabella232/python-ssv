import grpc
import time
from concurrent import futures
from google.protobuf.empty_pb2 import Empty
import python_ssv.rpc.validator_pb2_grpc as validator_pb2_grpc
import python_ssv.rpc.validator_pb2 as validator_pb2
import python_ssv.rpc.attestation_pb2 as attestation_pb2


class BeaconMock(validator_pb2_grpc.BeaconNodeValidatorServicer):

    def __init__(self, port):
        self.port = port

    def DomainData(self, request, context):
        return validator_pb2.DomainResponse(signature_domain=bytes.fromhex('01000000'))

    def StreamDuties(self, request, context):
        # TODO add rest of stuff to response
        duty = validator_pb2.DutiesResponse.Duty(committee=[0],committee_index=0,attester_slot=0,
                proposer_slots=0,validator_index=0) 
        yield validator_pb2.DutiesResponse(duties=[duty], current_epoch_duties=[duty], next_epoch_duties=[duty])
        time.sleep(10)


    def WaitForSynced(self, request, context):
        yield validator_pb2.SyncedResponse(synced=True, genesis_time=int(time.time()))
        return


    def GetAttestationData(self, request, context):
        source = attestation_pb2.Checkpoint(epoch = 0, root = bytes.fromhex("87654321"))
        target = attestation_pb2.Checkpoint(epoch = 0, root = bytes.fromhex("12344321"))
        return attestation_pb2.AttestationData(
                slot=0,
                committee_index=0,
                beacon_block_root=bytes.fromhex("12345678"), # fake root 
                source = source,
                target = target)


    def ProposeAttestation(self, request, context):
        return validator_pb2.AttestResponse(attestation_data_root = bytes.fromhex("87655678"))


    def SubscribeCommitteeSubnets(self, request, context):
        return Empty()

    def startServer(self):
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        validator_pb2_grpc.add_BeaconNodeValidatorServicer_to_server(self, server)
        server.add_insecure_port(f'[::]:{self.port}')
        server.start()
        print("Server started!")
        server.wait_for_termination()

