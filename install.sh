#!/bin/bash

apt install -y python3-venv
git clone https://github.com/CyberKuk/net-sender.git ~/sender
cd ~/sender
cp .env.dist .env
chmod a+x ./run.sh

python3 -m venv ./net_sender
source /root/sender/net_sender/bin/activate
python3 -m pip install --upgrade pip
pip install python-dotenv
pip install python-telegram-bot
deactivate

cp net-sender.service /etc/systemd/system/net-send.service
systemctl enable net-send.service
