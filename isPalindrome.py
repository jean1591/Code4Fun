
def isPalindrome():
    """
    Checks if a given string is a palindrome
    return bool: True if palindrome, False otherwise
    """
    
    string = input("Enter a string:\t")
    
    if string.lower() == string[::-1].lower():
        print("\"", string.upper(), "\" is a palindrome")
        return True
    print("\"", string.upper(), "\" is not a palindrome")
    return False

isPalindrome()