
# Dict from letter to morse
letterToMorse = {'A': '.-', 'B': '-...', 'C': '-.-.',
       'D': '-..', 'E': '.', 'F': '..-.',
       'G': '--.', 'H': '....', 'I': '..',
       'J': '.---', 'K': '-.-', 'L': '.-..',
       'M': '--', 'N': '-.', 'O': '---',
       'P': '.--.', 'Q': '--.-', 'R': '.-.',
       'S': '...', 'T': '-', 'U': '..-',
       'V': '...-', 'X': '-..-', 'Y': '-.--',
       'Z': '--..-',
       '0': '-----', '1': '.----', '2': '..---',
       '3': '...--', '4': '....-', '5': '.....',
       '6': '-....', '7': '--...', '8': '---..',
       '9': '----.'
       }

# Dict from morse to letter
morseToLetter = dict(zip(letterToMorse.values(), letterToMorse.keys()))


def decodeMsg(string):
    """
    Decode morse code to letters
    @param: str string: string to decode
    return str: message decoded
    """
    msg = ""
    lst = string.split(" ")
    
    for e in lst:
        try:
            msg += morseToLetter[e]
        except KeyError:
            msg += " "
    
    return msg[0:-1]


def encodeMsg(string):
    """
    Encode letters to morse code
    @param: str string: string to encode
    return str: message encoded
    """
    msg = ""
    
    for e in string:
        try:
            msg += letterToMorse[e] + " "
        except KeyError:
            msg += " "
    
    return msg


def assertEquals(test1, test2):
    return test1 == test2


def tests():
    test1 = "ABC DE FGH"
    msgCode1 = encodeMsg(test1)
    msgDecode1 = decodeMsg(msgCode1)
    if not assertEquals(test1, msgDecode1):
        print("Test1 failed")
        return False
    
    test2 = "123 45 6789 0"
    msgCode2 = encodeMsg(test2)
    msgDecode2 = decodeMsg(msgCode2)
    if not assertEquals(test2, msgDecode2):
        print("Test2 failed")
        return False
    
    test3 = "1A2B 3C 4D5E6F 7G8H"
    msgCode3 = encodeMsg(test3)
    msgDecode3 = decodeMsg(msgCode3)
    if not assertEquals(test3, msgDecode3):
        print("Test3 failed")
        return False
    
    return True

tests()