#!/bin/bash
# post json body shower
curl -sX POST -H "Content-Type: application/json" -d @"$2" "$1"
