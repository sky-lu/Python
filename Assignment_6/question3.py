'''
Write a Python program that sum the length of the names of a given 
list of names after removing the names that starts with a lowercase 
letter. Use lambda function. In the other, find the length of the names starts with uppercase.
'''
sample_names = ['sally', 'Dylan', 'rebecca', 'Diana', 'Joanne', 'keith']
names = list(filter(lambda n: n[0].isupper() and n[1:].islower(), sample_names))
print("Result:")
print(len(''.join(names)))