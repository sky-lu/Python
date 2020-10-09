'''
---Given an input string Count all lower case, upper case, digits, and special symbols---
for loop and methods of string
'''

str1 = "jfT6#0w12$%"
L_charCount = 0
U_charCount = 0
digitCount = 0
symbolCount = 0
for char in str1:
    if char.islower():
        L_charCount += 1
    elif char.isupper():
        U_charCount += 1
    elif char.isnumeric():
        digitCount += 1
    else :
        symbolCount += 1

print("Lower case =",L_charCount)
print("Upper case =",U_charCount)
print("digitCount =",digitCount)
print("symbolCount",symbolCount)
