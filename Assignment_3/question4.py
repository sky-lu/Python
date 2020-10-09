'''
---Given an input string, count occurrences of all characters within a string---
string methood---str.count() + dictionary data type (key-value)
'''

str1 = "pynativepynvepynative"
countDict = dict()
for char in str1 :
    count = str1.count(char)
    countDict[char] = count
print(countDict)
