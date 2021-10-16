#!/bin/bash

sudo apt-get install python3

python3 -m venv venv

source venv/bin/activate

pip install -r requirements.txt

cd app

echo "Complete Installing!!"
echo ""
echo "Starting: $ uvicorn main:app --reload"
echo "----------------------------"
echo "Ending  : [Ctrl + c]"
echo "Ending  : $ deactivate"
