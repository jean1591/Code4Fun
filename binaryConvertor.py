
from math import pow
from random import randint

def convertToBinary(num):
    """
    Convert a decimal number to binary
    @param: num as int, number to convert
    @return: str, converted number
    """

    # print("Convert {num} into binary".format(num=num))
    result = ""
    
    whole = num
    while (whole > 0):
        # print("{whole} / 2 = {int} with a remainder of {remainder}".format(whole=whole, int=int(whole/2), remainder=int(whole%2)))
        result = str(int(whole%2)) + result
        whole = int(whole/2)

    return result


def convertFromBinary(num):
    """
    Convert a binary number to decimal
    @param: num as str, number to convert
    @return: int, converted number
    """

    # print("Convert {num} from binary".format(num=num))
    result = int()

    n = len(num)-1
    for element in num:
        # print("{element} * 2^{n} = {total}".format(element=element, n=n, total = int(element) * pow(2, n)))
        result += (int(element) * pow(2, n))
        n-=1
    
    return int(result)


def testCases():
    for element in range(10000):
        asBinary = convertToBinary(element)
        asDecimal = convertFromBinary(asBinary)
        msg = "| {num:15} | {asBinary:15} | {asDecimal:15} |".format(num=element, asBinary=asBinary, asDecimal=asDecimal)
        assert element == asDecimal, msg
        print(msg)

testCases()