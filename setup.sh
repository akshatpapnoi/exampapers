#!/bin/sh

sudo apt-get update
sudo apt-get install python3.6 python3-pip 
sudo apt install build-essential libssl-dev libffi-dev python3-dev
sudo apt install -y python3-venv


python3 -m venv virtualenv
source virtualenv/bin/activate
pip3 install -r requirements.txt
deactivate
