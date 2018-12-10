
dct = {
       "10 2 +": 12,
       "10 2 *": 20,
       "10 2 -": 8,
       "10 2 /": 5,
       "10 2 + 5 *": 60,
       "10 2 * 4 /": 5,
       "10 2 + 2 -": 10,
       "10 2 * 20 +": 40,
       "6 2 * 3 / 6 + 10 *": 100
       }

def assertEquals(elem1, elem2):
    return elem1 == elem2

def calc(str):
    lst = str.split(" ")
    lstInt = []
    result = 0
    
    for element in lst:
        try:
            lstInt.append(int(element))
        except ValueError:
            if element == "+":
                result = lstInt[0] + lstInt[1]
            elif element == "*":
                result = lstInt[0] * lstInt[1]
            elif element == "-":
                result = lstInt[0] - lstInt[1]
            elif element == "/":
                result = lstInt[0] / lstInt[1]
            lstInt[0] = result
            lstInt.pop()

    return result

def tests(dct):
    for element in dct:
        if not (assertEquals(calc(element), dct[element])):
            print("Test failed on: ", element)
            return False
    return True

tests(dct)