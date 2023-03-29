#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Recursive Python program to calculate the greatest common divisor of two numbers.

@File = gcd.py
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


# main entry point
if len(sys.argv) != 3:
    print("Usage: python gcd.py <number1> <number2>")
    sys.exit(1)

print(gcd(int(sys.argv[1]), int(sys.argv[2])))
