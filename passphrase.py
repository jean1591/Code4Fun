#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import string
alpha = string.ascii_lowercase
digits = string.digits
# print(digits)

def complexify(passphrase, key):
    """
    Takes a passphrase as input, and return a crypted passphrase
    @param: passphrase, str, passphrase to crypt
    @param: key, int, number of shifts in the alphabet
    return: str, crypted passphrase
    """
    
    count = 0
    newPassphrase = ""
    
    # Run through elements in passphrase
    for element in passphrase:
        
        # If element is alpha
        if element in alpha:
            # Shift into alphabet
            currentIndex = alpha.index(element)
            # Loop back into alphabet
            newIndex = (currentIndex + key) % 26
            # If count is even, letter are lowercase
            if count % 2 == 0:
                newPassphrase += alpha[newIndex].lower()
            # If count is odd, letters are uppercase
            else:
                newPassphrase += alpha[newIndex].upper()
        
        # If element is numeric
        elif element in digits:
            # Get the complement to 9
            newPassphrase += str((9 - int(element)))
        
        # If element is not alphanumeric, no changes
        else:
            newPassphrase += element
        
        # Increment count
        count += 1
    
    # Return reverse result
    return newPassphrase[::-1]
        

print(complexify("abc.xyz-- 159", 1))
print(complexify("abc.xyz-- 159", 26))