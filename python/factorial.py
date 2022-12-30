#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Recursive Python programm to calculate the factorial of a given number.

@File = factorial.py
@Date = 2022-12-28
@Author = Jannis Metrikat
@Version = 1.0

"""

import sys

# calculates the factorial of a given number
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


# main entry point
if len(sys.argv) != 2:
    print("Usage: python factorial.py <number>")
    sys.exit(1)

n = sys.argv[1]
print(factorial(int(n)))
