#!/usr/bin/python3
"""
Script that takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user
"""
import requests
import sys

if __name__ == '__main__':
    try:
        letter = sys.argv[1]
    except IndexError:
        letter = ""
    url = 'http://0.0.0.0:5000/search_user'
    data = {'q': letter}
    response = requests.post(url, data=data)
    try:
        json_response = response.json()
        if json_response:
            print("[{}] {}".format(
                   json_response.get('id'), json_response.get('name')))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
