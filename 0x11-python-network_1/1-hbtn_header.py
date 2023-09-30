#!/usr/bin/python3
# Python script that takes in a URL, sends a request to the URL and displays the value

if __name__ == '__main__':
    import urllib.request
    from sys import argv

    with urllib.request.urlopen(argv[1]) as response:
        head = response.headers.get('X-Request-Id')
        print(head)
