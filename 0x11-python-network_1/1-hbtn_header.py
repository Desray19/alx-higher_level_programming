#!/usr/bin/python3
"""it sends a request with url"""

from urllib import request
from sys import argv

if __name__ == "__main__":
    with request.urlopen(argv[1]) as page:
        print(page.getheader("X-Request-Id"))
