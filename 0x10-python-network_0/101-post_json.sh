#!/bin/bash
#Write a Bash script that sends a JSON POST request
curl -s --jeson @- "$1" < "$2"
