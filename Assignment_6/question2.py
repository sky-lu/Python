'''
Write a Python program to find intersection of two given arrays using Lambda
'''
num1 = [1, 2, 3, 5, 7, 8, 9, 10]
num2 = [1, 2, 4, 8, 9]
result = list(filter(lambda x : x in num1, num2))
print("Intersection of the said arrays:", result)