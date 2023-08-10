#!/bin/bash

# Redirect output to a log file
exec &> script_log.txt

# Execute the first Python script
python /Users/ischneid/chat-gpt-us-state-dialectology/main.py

# Execute the second Python script
python /Users/ischneid/chat-gpt-us-state-dialectology/aggregate.py