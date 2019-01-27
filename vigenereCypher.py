#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 11:33:52 2019

@author: jean
"""

import string
import re

alphabet = string.ascii_lowercase

def vigenereCypher(msg, key):
    """
    Vigenere cypher code
    param: msg, str, message to code
    param: key, str, shift value 
    returm: str, coded message
    """
    # Strip all non-alpha
    msg = stripNonAlpha(msg)
    
    # Init variables
    result = ""
    count = 0
    line = 0
    
    for element in range(len(msg)):
        # Separates letters by group of 5 letters
        if count % 5 == 0 and count != 0:
            result += " "
            line += 1
        # Separates lines by groups of 5 packages of letters
        if line % 5 == 0 and line != 0:
            result += "\n"
            line = 0
        # Find index of current letter
        currentLetter = msg[element]
        indexLetter = alphabet.find(currentLetter.lower())
        # Find index of current key letter
        currentKey = key[element % len(key)]
        indexKey = alphabet.find(currentKey.lower())
        # Find index of shifted letter
        newIndex = (indexLetter + indexKey) % 26
        # Add the shifted letter to result
        result += alphabet[newIndex].upper()
        count += 1
    
    # Add extra "-" at the end of the coded message
    if count % 5 != 0:
        addN = 5 - (count % 5)
        for element in range(addN):
            result += "-"
    
    return result
        

def stripNonAlpha(msg):
    """
    Strips all non-alpha characters from a string
    param: str, message to strip of all non-alpha characters
    return: str, msg with only alpha characters
    """
    regex = re.compile("[^a-zA-Z]")
    return regex.sub("", msg)


def vigenereDecypher(msg, key):
    """
    Decypher caesar code
    param: msg, str, message to decypher
    param: key, str, shift value 
    return: str, decyphered message
    """
    
    # Strip all non-alpha
    msg = stripNonAlpha(msg)
    
    # Init variables
    result = ""
    count = 0
    line = 0
    
    for element in range(len(msg)):
        # Separates letters by group of 5 letters
        if count % 5 == 0 and count != 0:
            result += " "
            line += 1
        # Separates lines by groups of 5 packages of letters
        if line % 5 == 0 and line != 0:
            result += "\n"
            line = 0
        # Find index of current letter
        currentLetter = msg[element]
        indexLetter = alphabet.find(currentLetter.lower())
        # Find index of current key letter
        currentKey = key[element % len(key)]
        indexKey = alphabet.find(currentKey.lower())
        # Find index of shifted letter
        newIndex = (indexLetter - indexKey) % 26
        # Add the shifted letter to result
        result += alphabet[newIndex].upper()
        count += 1
    
    # Add extra "-" at the end of the coded message
    if count % 5 != 0:
        addN = 5 - (count % 5)
        for element in range(addN):
            result += "-"
    
    return result


print("INITIAL STRING:")
toCode = "Strips all non-alpha characters from a string param: str, message to strip of all non-alpha characters return: str, msg with only alpha characters"
print(toCode)

print("\nCODED MESSAGE:")
toDecode = vigenereCypher(toCode, "LEMON")
print(toDecode)

print("\nDECODED MESSAGE:")
decoded = vigenereDecypher(toDecode, "LEMON")
print(decoded)