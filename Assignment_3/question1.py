'''
---arrange String characters such that lowercase letters should come first---
string method: islower(),isupper()----Determine whether lowercase, uppercase
When the element connector in join() is specified as empty, 
each element of the iterable object will be formed into a connected string 
'''
s1 = "PyNaTive"
lower = []
upper = []
for char in s1:
    if char.islower():
        lower.append(char)
    else :
        upper.append(char)
s2 = ''.join(lower + upper)
print(s2)
