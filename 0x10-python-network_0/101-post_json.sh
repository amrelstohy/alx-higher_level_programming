#!/bin/bash
#Write a Bash script that sends a JSON POST request
curl -s -X POST --jeson "$2" "$1"
