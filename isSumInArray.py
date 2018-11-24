#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 18 15:18:24 2018

@author: jean

Looks in an array if two numbers add up to a defined number, use different 
algo to check efficiency
"""

arr1 = [1, 2, 3, 4]
arr2 = [1, 2, 4, 4]


def naiveAlgo(arr, result):
    """
    Naive algo, looks at each element and loop through array looking for
    second element that adds up to result
    @param: arr, int[]
    @param: result: int
    """
    step = 0
    # Run through the list
    for i in range(0, len(arr)):
        step+=1
        # Run through the list from i
        for j in range(i, len(arr)):
            step+=1
            if arr[i] + arr[j] == result:
                return arr[i], arr[j], step
    else:
        return 0


def binaryAlgo(arr, result):
    """
    Algo that loops through the array once, looking for element that adds up to
    result with a binary search
    @param: arr, int[]
    @param: result: int
    """
    step = 0
    for i in range(len(arr)):
        step+=1
        toResult = result - arr[i]
        binaryTest = binarySearch(arr, toResult)
        if binaryTest[0] >= 0:
            step += binaryTest[1]
            return arr[i], arr[binaryTest[0]], step
    return 0
            

def binarySearch(arr, num):
    step = 0
    trouve = False
    indDebut = 0
    indFin = len(arr)
    
    while trouve is False and indFin - indDebut > 1:
        step+=1
        indMilieu = int((indFin + indDebut) / 2)
        trouve = arr[indMilieu] == num
        
        if indMilieu > num:
            indFin = indMilieu
        else:
            indDebut = indMilieu
    
    if arr[indDebut] == num:
        return indDebut, step
    else:
        return -1, step


def twoEndsSearch(arr, result):
    """
    Algo that starts at each ends of the array, adds up the two element, if sum
    is greater than result, moves up the array, if sum is less than result,
    moves down the array. Stop when result is found or when the ends meet
    @param: arr, int[]
    @param: result: int
    """
    step = 0
    smallInd = 0
    bigInd = int(len(arr)-1)
    trouve = False
    
    while trouve is False and smallInd != bigInd:
        step+=1
        score = arr[smallInd] + arr[bigInd]
        trouve = score == result
        if score > result:
            bigInd-=1
        else:
            smallInd+=1
    if trouve:
        return arr[smallInd], arr[bigInd], step
    else:
        return 0



testNumber = 6
print("TESTED NUMBER:\t\t", testNumber)
print("NAIVE ALGO:\t\t", naiveAlgo(arr2, testNumber))
print("BINARY ALGO:\t\t", binaryAlgo(arr2, testNumber))
print("TWO ENDS SEARCH:\t", twoEndsSearch(arr2, testNumber))