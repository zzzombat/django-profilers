#!/usr/bin/env python

import sys
from wsgiref.simple_server import make_server

if __name__ == "__main__":
    execfile(sys.argv[1])
    httpd = make_server('', 8000, application)
    httpd.serve_forever()