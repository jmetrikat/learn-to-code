#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Recursive Py.

@File = lcm.py
@Date = 2023-03-29
@Author = Jannis Metrikat
@Version = 1.0

"""

import sys


# calculate the greatest common divisor using euclid's algorithm
def gcd(a: int, b: int) -> int:
    if b == 0:
        return a

    return gcd(b, a % b)


# calculate the least common multiple using greatest common divisor
def lcm(a: int, b: int) -> int:
    return int((a * b) / gcd(a, b))


# main entry point
if len(sys.argv) != 3:
    print("Usage: python lcm.py <number1> <number2>")
    sys.exit(1)

print(lcm(int(sys.argv[1]), int(sys.argv[2])))
