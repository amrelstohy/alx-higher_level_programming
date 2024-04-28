#!/bin/bash
#Write a Bash script that sends a JSON POST request
curl -s "$1" -X POST -H "Content-Type: application/json" -d @"$2"
