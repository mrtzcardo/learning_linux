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

## JSON File Location
https://support.oneskyapp.com/hc/en-us/articles/208047697-JSON-sample-files <- that's the link to the webpage with the example_1.json

## Key Commands
cd - change directory. ex. cd /home/user/Desktop
ls - list everything in current directory ls
mkdir - make directory mkdir database
cp - copy from to copy frome-source to-destination
wget - download file from internet wget http://google.com/example.txt
top - show top process top
pgrep - get PIDs that match application pgrep chrome
cat - list contents of file cat example_1.json
nano - file editor nano text.txt
vi/vim - file editors vim test.txt
rm - remove object rm text.txt
sudo - execute as root sudo rm text.txt
chmod - change file system access chmod +x executable.sh
ssh - connect to a linux machine ssh user@123.456.789.101

## Subsystem for Linux Video
Developing on Windows with WSL2 (Subsystem for Linux), VS Code, Docker, and the Terminal 
https://youtu.be/A0eqZujVfYU
