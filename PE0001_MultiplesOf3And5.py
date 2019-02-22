
"""
Project Euler - Problem 0001
https://projecteuler.net/problem=1

If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""


def sumOfMultiples(num):
    """
    Calculates the sum of the multiples of 3 or 5 up to num
    @param: num: int, upper bound
    @return: total: int, sum of all the multiples
    """

    # Init total
    total = 0

    # Loop from 0 to num exclusive
    for element in range(num):
        # Add element to total if element is divisible by 3
        if element % 3 == 0:
            total += element
        # Add element to total if element is divisible by 5
        elif element % 5 == 0:
            total += element
    
    return total

print(sumOfMultiples(10))
print(sumOfMultiples(1000))
