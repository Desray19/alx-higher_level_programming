#!/bin/bash
# shows body and si
curl -so /dev/null -w '%{size_download}\n' "$1"
