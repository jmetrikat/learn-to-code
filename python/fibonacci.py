#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Python programm utilizing memoization to calculate the fibonacci sequence of a given number.

@File = fibonacci.py
@Date = 2023-03-29
@Author = Jannis Metrikat
@Version = 1.0

"""

import sys


# calculate the fibonacci sequence of a given number
def fibonacci(n: int) -> int:
    fib = [0 for i in range(n+2)]

    fib[0] = 0
    fib[1] = 1

    for i in range(2, n+1):
        fib[i] = fib[i-1] + fib[i-2]

    return fib[n]


# main entry point
if len(sys.argv) != 2:
    print("Usage: python fibonacci.py <number>")
    sys.exit(1)

if int(sys.argv[1]) < 0:
    print("Number must be positive.")
    sys.exit(1)

print(fibonacci(int(sys.argv[1])))
