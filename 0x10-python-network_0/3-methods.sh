#!/bin/bash
# http accept shower
curl -sI "$1" | grep "Allow" | cut -d' ' -f2-
