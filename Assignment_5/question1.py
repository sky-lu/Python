'''
Question 1: Write a program to calculate factorial of a number 
(note: you could create a recursive function to calculate factorial).
 In addition, you need to write a decorator named time_calculator to 
 calculate duration taken by factorial / any other function. 
 Hint: import time module and use time.time() to retrieve beginning 
 and ending (end – begin ) and display total time taken by factorial function.
'''

import time 
import math

def time_calculator(func):
    def wrapper(*args, **kwargs):
        begin = time.time()
        func(*args, **kwargs)
        end = time.time()
        print("Total time taken in : ", func.__name__, end - begin)

    return wrapper

@time_calculator
def factorial(num):
    time.sleep(2)
    print(math.factorial(num))
'''
def recur_factorial(num):
    if num == 1:
        return num
    else:
        return num * recur_factorial(num-1)
'''


factorial(5)