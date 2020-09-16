s1 = "my favourite fruit"
s2 = "apple"
a = int(len(s1)//2)
s3 = s1[:a] + s2 + s1[a:]
print(s3)