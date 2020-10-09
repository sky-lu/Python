'''
---Given a list iterate it and count the occurrence of each element and create a dictionary to show the count of each element---
for loop + if condition statement + distinguish from question4
'''

lst1 = [10, 20, 30, 10, 20, 40, 50]
countDict = dict()
for item in lst1 :
    if item in countDict :
       countDict[item] += 1
    else :
       countDict[item] = 1

print(countDict)