
def usernameGenerator():
    """
    Asks the user for its complete name and creates a username
    from it
    return str: username
    """
    
    # Ask for user's name and surname
    name = input("Enter your name:\t")
    surname = input("Enter your surname:\t")
    
    # Convert to lower case
    nGen = name.lower()
    sGen = surname.lower()
    
    # Calculate length
    totalLength = len(nGen) + len(sGen)
    
    # If length > 15
    if totalLength > 15:
        print("Full name is too long, proposed username:")
        
        # Check if name is too long
        if len(nGen) >= 7:
            # If yes, nGen is name's 1st letter
            nGen = name[0].lower()
        
        # Check for spaces in surname
        if " " in sGen:
            sGen = ""
            ind = 0
            while ind < len(surname):
                if surname[ind] != " ":
                    sGen += surname[ind].lower()
                else:
                    # Delete spaces and add uppercase letter
                    # for next letter
                    sGen += surname[ind+1].upper()
                    ind += 1
                ind += 1
    
    return nGen + "." + sGen

print(usernameGenerator())