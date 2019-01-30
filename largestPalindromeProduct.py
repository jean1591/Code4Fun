#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def largestPalindromicNumber(intNumber):
    """
    Return a palindrome number that is the product of two numbers of maximum intNumber digits
    @param: intNumber, int: maximum number of digits
    """
    # Find largest number possible
    maxValue = largestNumberPossible(intNumber)
    
    # Loop from the maxValue to 0
    for element in range(maxValue)[::-1]:
        # Return element if element is palindromic and is the product of a pair of numbers
        if isPalindromic(element) and isProduct(element, intNumber) != (0, 0):
            return element


def largestNumberPossible(intNumber):
    """
    Returns the largest product possible given a number of digits
    @param: intNumber, int: maximum number of digits
    """
    n = ""
    for element in range(intNumber):
        n += "9"
    n = int(n)
    return n * n


def isPalindromic(number):
    """
    Returns true if a number is a palindrome, false otherwise
    @param: number, int: tested number
    """
    return str(number) == str(number)[::-1]


def isProduct(number, intNumber):
    """
    Returns a pair of numbers if their product equals the given number
    @param: number, int: tested number
    @param: intNumber, int: maximum authorised number of digits
    """
    result = (0, 0)
    
    upBound = 1;
    for element in range(intNumber):
        upBound = upBound * 10
    upBound += 1

    for i in range(2, upBound)[::-1]:
        for j in range(2, upBound)[::-1]:
            if i * j == number:
                return (i, j)
    return result


print("===========================")
print("LARGEST PALINDROMIC NUMBER:")
print("Two Digits:\t ", end = "")
print(largestPalindromicNumber(2))
print("Three Digits:\t ", end = "")
print(largestPalindromicNumber(3))
print("===========================")