import string


def findPwd(pwd):
    alpha = list(string.ascii_lowercase)
    count = 0

    while (count < 10):
        
        count+= 1
    print(pwd)

def rotateAlphabet(key):
    alpha = list(string.ascii_lowercase)
    return alpha[key:] + alpha[:key]

