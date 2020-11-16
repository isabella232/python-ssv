#!/bin/bash

tmux \
  new-session  "python run.py 0 --port 50051 --beacon_rpc 127.0.0.1:60000 --validators conf/validators.json; read" \; \
  split-window  "python run.py 1 --port 50052 --beacon_rpc 127.0.0.1:60000 --validators conf/validators.json; read" \; \
  split-window  "python run.py 2 --port 50053 --beacon_rpc 127.0.0.1:60000 --validators conf/validators.json; read" \; \
  split-window  "python run.py 3 --port 50054 --beacon_rpc 127.0.0.1:60000 --validators conf/validators.json; read" \; \
  split-window "bash util/wait.sh" \; \
  select-layout tiled
