#!/bin/bash

tmux \
  new-session  "python ssv_node.py 0 --port 50051 --beacon_rpc localhost:6000 --validators conf/validators.json --privkey conf/threshold_key_0.json; read" \; \
  split-window  "python ssv_node.py 0 --port 50052 --beacon_rpc localhost:6000 --validators conf/validators.json --privkey conf/threshold_key_1.json; read" \; \
  split-window  "python ssv_node.py 0 --port 50053 --beacon_rpc localhost:6000 --validators conf/validators.json --privkey conf/threshold_key_2.json; read" \; \
  split-window  "python ssv_node.py 0 --port 50054 --beacon_rpc localhost:6000 --validators conf/validators.json --privkey conf/threshold_key_3.json; read" \; \
  split-window "bash wait.sh" \; \
  select-layout tiled
