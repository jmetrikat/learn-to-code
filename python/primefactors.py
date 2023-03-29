#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Python program to calculate prime factors of a given number.

@File = primefactors.py
@Date = 2023-03-29
@Author = Jannis Metrikat
@Version = 1.0

"""

import sys


# calculate prime factors of a given number
def primefactors(n: int) -> None:
    found_factor = False

    for i in range(2, n):
        is_prime = True

        for j in range(2, i):
            if i % j == 0:
                is_prime = False
                break

        if n % i == 0 and is_prime:
            print(i)
            found_factor = True

    if not found_factor:
        print(str(n) + " is prime.")

    return


# main entry point
if len(sys.argv) != 2:
    print("Usage: python primefactors.py <number>")
    sys.exit(1)

if int(sys.argv[1]) < 2:
    print("Number must be greater than 1.")
    sys.exit(1)

primefactors(int(sys.argv[1]))
