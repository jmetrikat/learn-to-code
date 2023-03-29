#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Python program to calculate all prime numbers up to a given number.

@File = primes.py
@Date = 2023-03-29
@Author = Jannis Metrikat
@Version = 1.0

"""

import sys


# calculate primes using the sieve of eratosthenes
def primes(n: int) -> None:
    is_prime = [True for _ in range(n + 1)]

    for i in range(2, n + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False

    for i in range(2, n + 1):
        if is_prime[i]:
            print(i)

    return


# main entry point
if len(sys.argv) != 2:
    print("Usage: python primes.py <number>")
    sys.exit(1)

if int(sys.argv[1]) < 2:
    print("Number must be greater than 1.")
    sys.exit(1)

primes(int(sys.argv[1]))
