'''
Write a Python program to add two given lists and find the sum and 
difference between lists. Use map () function.
'''
lst1 = [6, 5, 3, 9]
lst2 = [0, 1, 7, 7]
result = map(lambda x, y:(x + y, x - y), lst1, lst2)
print(list(result))
