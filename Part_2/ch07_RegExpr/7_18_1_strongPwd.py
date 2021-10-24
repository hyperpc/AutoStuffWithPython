#! python3

# strong requirement:
# - length >= 8
# - include characters in UpperCase and LowerCase
# - at least 1 number
import re

def CheckPwd():
    print('Enter your token:')
    pwd = input()
    if len(pwd) < 8:
        print('Error: length lower than 8')
        return False
    
    lowerCaseRegex = re.compile(r'[a-z]+')
    lowerMatch = lowerCaseRegex.search(pwd)
    print(lowerMatch)
    if lowerMatch == None:
        print('Error: not found lower case character')
        return False
    print(lowerMatch.group())

    upperCaseRegex = re.compile(r'[A-Z]+')
    upperMatch = upperCaseRegex.search(pwd)
    print(upperMatch)
    if upperMatch == None:
        print('Error: not found upper case character')
        return False
    print(upperMatch.group())

    numberRegex = re.compile(r'\d+')
    numberMatch = numberRegex.search(pwd)
    print(numberMatch)
    if numberMatch == None:
        print('Error: not found numbers')
        return False
    print(numberMatch.group())
    print('Success')
    return True

CheckPwd()