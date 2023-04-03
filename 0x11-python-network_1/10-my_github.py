#!/usr/bin/python3
"""
Takes your GitHub credentials (username and password) and uses the GitHub API
to display your id
"""
import requests
import sys

if __name__ == "__main__":
    # Get the command line arguments
    username = sys.argv[1]
    password = sys.argv[2]

    # Send a GET request to the GitHub API
    response = requests.get(
       "https://api.github.com/user", auth=(username, password))

    # Check if the response was successful (status code between 200-299)
    if response.status_code in range(200, 300):
        # Get the JSON data from the response
        data = response.json()
        # Display the user's id
        print(data['id'])
    else:
        # Display the error status code
        print("None")
