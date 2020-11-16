#!/bin/bash
virtualenv venv -p `which python3`
. venv/bin/activate
pip install -r requirements.txt
pip install ./python-ibft
pip install .
