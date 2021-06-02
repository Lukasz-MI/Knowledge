setNumbers = {2,5,10,22,42,65}

setNumbers.add (64)

print (setNumbers) # {64, 65, 2, 42, 5, 22, 10}

setNumbers.discard(42)
print(type(setNumbers)) # <class 'set'>
print(setNumbers) # {64, 65, 2, 5, 22, 10}

for v in setNumbers:
    print(v)

frozenData = frozenset(setNumbers)
print(type(frozenData)) # <class 'frozenset'>

# frozenData.add (102) # Numbers cannot be added to frozenset

for numbers in frozenData:
    print(numbers)

'''
Result:

64
65
2
5
22
10
'''

