#!/bin/bash
#a Bash script that displays all HTTP methods the server will accept.
curl -sI -X OPTIONS "$1" | grep -i "Allow:"
