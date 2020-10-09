sampleList = [87, 45, 41, 65, 94, 41, 99, 94]
list1 = list(set(sampleList))
list1.sort()
print(list1)
t1 = tuple(list1)
print("The minimum number is", t1[0])
print("The maximum number is", t1[len(t1)-1])