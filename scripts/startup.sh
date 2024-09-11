#!/bin/bash

SCRIPT="/home/piandrej/Repositories/PyAssist/main.py"

# source /home/piandrej/Repositories/PyAssist/venv/bin/activate

/home/piandrej/Repositories/PyAssist/venv/bin/python $SCRIPT >> /home/piandrej/.pyassist/pyassist.log 2>&1
