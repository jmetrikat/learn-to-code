#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Recursive Python programm to calculate the factorial of a given number.

@File = factorial.py
@Date = 2022-12-28
@Author = Jannis Metrikat
@Version = 1.0

"""

#  Calculates the factorial of a given number.
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


# main entry point
n = input("Enter a number to find the factorial of: \n")
print(factorial(int(n)))
