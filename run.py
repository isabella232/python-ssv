import python_ssv
import argparse
import json


parser = argparse.ArgumentParser(description='Run SSV node.')
parser.add_argument('process_id', metavar='process_id', type=int, 
                    help='The ID of the process')
parser.add_argument('--parties', metavar='parties_json', type=str, default="python-ibft/conf/parties.json",
                    help='IBFT: JSON configuring the parties')
parser.add_argument('--config', metavar='config_json', type=str, default="python-ibft/conf/config.json",
                    help='IBFT: JSON configuration')
parser.add_argument('--privkey', metavar='privkey_json', type=str, default="",
                    help='IBFT: JSON configuration')
parser.add_argument('--port', metavar='port', type=int, default=50051,
                    help='Incoming RPC port')
parser.add_argument('--validators', metavar='validators_json', type=str, default="validators.json",
                    help='Validator configuration')
parser.add_argument('--beacon_rpc', metavar='beacon_rpc', type=str, default="localhost:4000",
                    help='Beacon RPC Node')

args = parser.parse_args()


process_id = args.process_id

# Load the combined as well as threshold public keys
# TODO: Currently only supports one key


keys_json = json.load(open(args.validators, "r"))
public_key = bytes.fromhex(keys_json[0]["public_key"])
threshold_public_keys = [bytes.fromhex(x) for x in keys_json[0]["threshold_public_keys"]]

parties = json.load(open(args.parties, "r"))
config = json.load(open(args.config, "r"))

# Load the private key
if args.privkey == "":
    privkey_file = "python-ibft/conf/privkey_{0}.json".format(process_id)
else:
    privkey_file = args.privkey

privkey = json.load(open(privkey_file, "r"))


python_ssv.init(args.beacon_rpc, process_id, parties, config, privkey, public_key, threshold_public_keys, args.port)
