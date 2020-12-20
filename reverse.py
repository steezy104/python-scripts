def reverse(string):
    '''Takes in a string and returns its reverse.
    '''
    newString = ""
    length = len(string)
    for i in range(length, 0, -1):
        newString += string[i - 1]
    return newString
    
print(reverse("Hello, World!"))