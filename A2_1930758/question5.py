rollNumber = [47, 64, 69, 37, 76, 83, 95, 97]
sampleDict = {'Jhon':47, 'Emma':69, 'Kelly':76, 'Jason':97}
s1 = set(rollNumber)
s2 = set(sampleDict.values())
s3 = s1.intersection(s2)
print(s3)