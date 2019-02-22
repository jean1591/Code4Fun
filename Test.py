

import math



def eratothenesSieve(num):
    """
    Implementatoion of Sieve of Eratosthenes
    @param: num: int, upper bound
    @return: primeNumbers: list, list of prime number from 2 to num inclusive
    """

    # List of prime numbers
    primeNumbers = []

    # Creates an array of size num where all values are True
    primes = [True for element in range(num+1)]

    # Init starting number
    currentNumber = 2
    # Loop from currentNumber to square root of num
    while currentNumber * currentNumber <= num:
        
        # Set all mutiples of currentNumber to False (not prime by definition)
        if primes[currentNumber]:
            # Loop from currentNumber * 2 to num with step = currentNumber
            for element in range(currentNumber * 2, num + 1, currentNumber):
                primes[element] = False
        
        # Increment currentNumber
        currentNumber += 1

    
    for element in range(2, num+1):
        # Add currentNumber to list of prime numbers
        if primes[element]:
            primeNumbers.append(element)
    
    return primeNumbers
    

print(eratothenesSieve(100))



