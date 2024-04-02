#!/bin/bash
# post body displayer sayng "you got me"
curl -s -X POST http://0.0.0.0:5000/catch_me -H "Content-Type: application/json" -d '{"data": "very secret data"}'

