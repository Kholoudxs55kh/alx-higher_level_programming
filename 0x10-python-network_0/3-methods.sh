#!/bin/bash
# displays the size of the body of the response to the URL using Curl
curl -sI ALLOW $1 -L | grep "Allow" | cut -d " " -f2-
