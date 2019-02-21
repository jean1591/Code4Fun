#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def smallestMultiple():
    
    dividedBy = [5, 6, 7, 8, 9]
    redLights = []
    for element in range(len(dividedBy)):
        redLights.append(False)
    
    count = 11
    while (True):
        greenLights = redLights.copy()
        if count == 3000:
            return False
        
        for element in range(len(dividedBy)):
            if (isDivisibleBy(count, dividedBy[element])):
                greenLights[element] = True
        
        if (all(element == True for element in greenLights)):
                return count
        count += 1
    

def isDivisibleBy(toDivide, dividedBy):
    return toDivide % dividedBy == 0


def isDivisibleByList(toDivide, dividedBy):
    # [5, 2]
    for element in dividedBy:
        # 10 / 5 & 10 / 2
        if toDivide % element != 0:
            return False
    return True


""" A TERMINER CI-DESSOUS """
"""
def findMultiplesToZero(number):
    result = []
    width = range(0, number+1)
    width = width[1:]
    
    for element in width[::-1]:
        print(element, end = ", ")
        if len(result) == 0:
            print("Not in list", True, end = ", ")
            result.append(element)
            continue
        
        if (not isDivisibleByList(element, result)):
            result.append(element)

    return result
"""
def findMultiplesToZero(number):
    result = []

    for element in range(number)[::-1]:
        for item in range(number):
            if item != 0 and item != 1 and element != 0 and element != item:
                # print(not isDivisibleBy(element, item))
                if (isDivisibleBy(element, item)):
                    continue
        result.append(element)

    return result

# print(smallestMultiple())
print(findMultiplesToZero(10))
# print([10, 8, 6, 5][(len([10, 8, 6, 5])-2)::-1])