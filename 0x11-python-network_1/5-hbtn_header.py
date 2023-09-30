#!/usr/bin/python3
""" Python script that takes in a URL, sends a request to the URL
"""
if __name__ == "__main__":
    from requests import get
    from sys import argv

    html = get(argv[1])
    print(html.headers.get('X-Request-Id'))
