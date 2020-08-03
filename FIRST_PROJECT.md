# BashScripts

## Overview
This project intent is to show the basic shell commands and how one can use bash scripts for recuring tasks on linux. 

## Steps 
- Set a user environment variable called `FILENAME_ENV` and set it to `example_1.json`
- create a bash script that 
1. Downloads a file from the internet and renames it to `example_local.json` (All in one command)
2. Displays the `FILENAME_ENV` environment variable
3. over writes environment variable to `example_local.json`
4. Displays the new contents of `FILENAME_ENV`
5. run a python script that changes the contents of the variable. The python script must use the environment variable to get the contents of the file
6. Display te contents of the overwritten file 
7. Displays `DONE.` when the process finishes 