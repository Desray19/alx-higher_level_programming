#!/bin/bash
# it passes the url request
curl -sX POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
