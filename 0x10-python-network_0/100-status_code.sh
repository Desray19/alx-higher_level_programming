#!/bin/bash
# status code shower
curl -so /dev/null -w '%{http_code}' "$1"
