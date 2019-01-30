#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def smallestMultiple():
    
    dividedBy = [6, 7, 8, 9, 10]
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

""" A TERMINER CI-DESSOUS """
def findMultiplesToZero(number):
    result = []
    
    for element in range(number)[::-1]:
        print()
        if element not in result:
            for items in result:
                if element % items == 0:
                    result.append(element)
    
    return result

# print(smallestMultiple())
print(findMultiplesToZero(10))