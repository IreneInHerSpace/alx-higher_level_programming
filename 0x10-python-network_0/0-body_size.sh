#!/bin/bash

# Check if a URL is provided
if [ -z "$1" ]; then
  echo "Usage: ./0-body_size.sh [URL]"
  exit 1
fi

# Send a request to the URL and store the response
response=$(curl -sI "$1")

# Extract the Content-Length header from the response
content_length=$(echo "$response" | grep -i "Content-Length" | awk '{print $2}' | tr -d '\r')

# Check if the Content-Length header is empty
if [ -z "$content_length" ]; then
  echo "Could not determine the size of the response body."
  exit 1
fi

# Print the size of the response body in bytes
echo "$content_length"
