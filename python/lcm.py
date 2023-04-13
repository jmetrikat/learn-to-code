#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Recursive Python program to calculate the least common multiple of two given numbers.

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

a = int(sys.argv[1])
b = int(sys.argv[2])

print(lcm(abs(a), abs(b)))
