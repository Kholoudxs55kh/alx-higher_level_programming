#!/usr/bin/python3
"""Python script that takes in a URL and an email address, sends a POST request
"""
if __name__ == "__main__":
    from requests import post
    from sys import argv

    html = post(argv[1], data={'email': argv[2]})
    print(html.text)
