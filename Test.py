#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from itertools import combinations 

arr = [715, 112, 136, 169, 144]


def isSquare(num):
    """
    Test if a number is a square or not
    @param: int num:    number to test
    return True if number is a square, False otherwise
    """
    # Number to increment
    n = 1
    # from itertools import combinations
    # While n squared is less than or equal to num
    while (n**2 <= num):
        # Test if n squared is equals to numand return True
        if n**2 == num:
            return True
        n+= 1
    return False


def swapeAndTestSquared(num):
    num = list(str(num))
    return list(combinations(num, len(num)))

print(swapeAndTestSquared(123))
    

"""
for element in arr:
    print(isSquare(element))
"""