firstSet = {27, 43, 34}
secondSet = {34, 93, 22, 27, 43, 53, 48}
print(firstSet.issubset(secondSet))
print(firstSet.issuperset(secondSet))
if firstSet.issubset(secondSet):
    firstSet.clear()
print(firstSet)