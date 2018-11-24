#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 20:56:20 2018

@author: jean

Returns the factorial of a given number
"""

def recursAlgo(num):
    if num < 2:
        return 1
    else:
        return num * recursAlgo(num-1)


print(recursAlgo(5))