#!/bin/bash
# Displays the body of the response of a curl POST request
curl -s 0.0.0.0:5000/catch_me?cmd=$(printf "printf\047You got me!\047")
