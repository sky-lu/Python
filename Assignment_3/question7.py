'''
---Write a Python program to construct the following pattern, using a nested for loop.---
range(start, stop, step)
end = " "--------end with space
'''
n = 5
for i in range(n) :
    for j in range(i):
        print ('*',end = "")
    print('')

for i in range(n,0,-1):
    for j in range(i):
        print('*',end = "")
    print('')

