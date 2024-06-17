#!/bin/bash

# get the directory path of the script
script_dir=$(dirname "$0")

# navigate to the directory where the snake game script is located
cd "$script_dir/src"

# run the snake game script using Python
python main.py
