# membership operators

data = [2,3,5,7,1,6]

print (2 in data) # True
print (9 not in data) # True - 9 is not in the list
print (8 in data) # False - not in the list

print ("Barbara" in ("Kate, Joanna, Barbara")) # True

# indetity operators

strData = "Care"
print (dir(strData))
print (strData.upper())

intData = 9
print (dir(intData))

a = [1,2,3,4,5]
b = a
print(a is b) # True - it refers to the same place in memory

a.append (62)
print(a) # [1, 2, 3, 4, 5, 62]
print(b) # [1, 2, 3, 4, 5, 62]

print (a is not b) # False - it means that nothing has changed "a" still has the same memory log as "b"

c = [3,4,5]
print (a is c) # False
print (a is not c) # True
