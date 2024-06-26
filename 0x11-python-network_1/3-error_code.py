#!/usr/bin/python3
""" it `sends request and display the page."""

from urllib import request, error
from sys import argv

if __name__ == "__main__":
    try:
        with request.urlopen(argv[1]) as page:
            print(page.read().decode('utf-8'))
    except error.HTTPError as e:
        print("Error code: {}".format(e.code))
