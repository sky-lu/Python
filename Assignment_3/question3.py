'''
---String characters balance Test---
for loop + if condition + flag variable
'''
s1 = "yn"
s2 = "Pynative"
flag = True
for char in s1 :
    if char in s2:
        continue
    else :
        flag = False
        break

print("s1 and s2 are balanced :", flag)
