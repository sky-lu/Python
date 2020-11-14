'''
Write a Python program to check whether a given string is a positive number or not using Lambda.
'''
#The isdigit() method returns True if all the characters are digits, otherwise False.
#string.replace(oldvalue, newvalue, count)
is_num1 = lambda n: n.replace('.', '', 1).isdigit()
is_num = lambda r : False if (r[0]== '-' and is_num1(r[1:])) else is_num1(r)
print(is_num('26587'))
print(is_num('4.2365'))
print(is_num('-12547'))
print(is_num('00'))
print(is_num('A001'))
print(is_num('001'))

