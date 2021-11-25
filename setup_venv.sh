#!/bin/bash
python3 -m venv validator-venv
source validator-venv/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip install -r python_dependencies.txt
ansible-galaxy install -r playbooks_dependencies.yml
