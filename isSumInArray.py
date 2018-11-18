#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 18 15:18:24 2018

@author: jean

Given an array of int and an int, finds if two numbers within the array sum up
to the int
"""

arr1 = [1, 2, 3, 4]
arr2 = [1, 2, 4, 4]
arr100 = range(100)


def naiveAlgo(arr, result):
    step = 0
    # Run through the list
    for i in range(0, len(arr)):
        step+=1
        # Run through the list from i
        for j in range(i, len(arr)):
            step+=1
            if arr[i] + arr[j] == result:
                return arr[i], arr[j]
    else:
        return 0


def binaryAlgo(arr, result):
    step = 0
    for i in range(len(arr)):
        step+=1
        toResult = result - arr[i]
        binaryTest = binarySearch(arr, toResult)
        print(binaryTest)
#        if binaryTest >= 0:
#            return arr[i], arr[binaryTest]
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
        return -1


def twoEndsSearch(arr, result):
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
        return arr[smallInd], arr[bigInd]
    else:
        return 0



testNumber = 8
print("TESTED NUMBER:\t\t", testNumber)
print("NAIVE ALGO:\t\t", naiveAlgo(arr2, testNumber))
print("BINARY ALGO:\t\t", binaryAlgo(arr2, testNumber))
print("TWO ENDS SEARCH:\t", twoEndsSearch(arr2, testNumber))