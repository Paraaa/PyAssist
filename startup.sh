#!/bin/bash

SCRIPT="$HOME/Repositories/PyAssist/main.py"

source $HOME/Repositories/PyAssist/venv/bin/activate

python $SCRIPT >> $HOME/.pyassist/pyassist.log 2>&1
