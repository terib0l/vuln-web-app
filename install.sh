#!/bin/bash

sudo apt-get install python3

pip install -r requirements.txt

cd app

echo "Complete Installing!!"
echo ""
echo "Starting: $ python3 manage.py runserver"
echo "----------------------------"
echo "Ending  : [Ctrl + c]"
