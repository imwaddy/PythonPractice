#!/usr/bin/python3


class DivideFiveException(Exception):
    def __init__(self, arg):
        self.arg = arg


try:
    raise DivideFiveException("Divide Five exception")
except DivideFiveException as d:
    print(d.arg)
