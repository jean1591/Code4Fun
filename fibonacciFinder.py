#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 21:05:25 2018

@author: jean

Given n, returns the nth Fibonacci's number
"""


def recursAlgo(num):
    if num <= 1:
        return num
    else:
        return recursAlgo(num-2) + recursAlgo(num-1)


def optimizedAlgo(num):
    if num <= 1:
        return num
    else:
        fib = [0, 1]
        for element in range(2, num+1):
            fib.append(fib[-2] + fib[-1])
    return fib[-1]

print(optimizedAlgo(10))
print(recursAlgo(10))
