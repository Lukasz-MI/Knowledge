# immutable: int, float, bool, str, tuple, frozenset

a = 1
addr1 = id(a)

a += 1
addr2 = id(a)

print (addr1) #2243938707760
print (addr2) #2243938707792 
print (addr1 == addr2) 
# False - diferent ids in immutable types

# mutable types: list, set, dict

data = [1, "Anne" , 30, "Henry"]

addr1 = id(data)
print(addr1) 

data += [33, "Monica" , 40] 
print (data)
addr2 = id(data)
print (addr2)

print (addr1 == addr2)  
 
# True - the same ids in mutable types

