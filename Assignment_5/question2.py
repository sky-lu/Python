'''
Write a Python program to convert all the characters in uppercase 
and lowercase and eliminate duplicate letters from a given sequence. 
Use map () function.
'''
seq = ['f', 'b', 'U', 'i', 'o', 'E', 'a']
result = map(lambda x:(x.upper(), x.lower()), seq)
print(list(result))

new_seq = []
def removeDuplicate(n):
    if (n not in new_seq):
        new_seq.append(n)
        return n
    
result1 = map(removeDuplicate, seq)
print(list(filter(None, result1)))


