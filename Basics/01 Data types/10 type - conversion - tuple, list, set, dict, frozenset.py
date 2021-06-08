List = [1,5,2,6,3,6,78,434,2235,3453]
print(List) # [1, 5, 2, 6, 3, 6, 78, 434, 2235, 3453]

tupleList = tuple(List)
print (tupleList) # (1, 5, 2, 6, 3, 6, 78, 434, 2235, 3453)
print(type(tupleList)) #  <class 'tuple'>

ListRandom = list (("Kate" , 32, "Jonathan", 30)) #  conversion to list - ['Kate', 32, 'Jonathan', 30]
print(ListRandom)

frozenSetOutOfList = frozenset(List) # straight away conversion from list to frozenset
print (type(frozenSetOutOfList)) # <class 'frozenset'>

tupleCombined = ( ("Ola" , 132) , ("Rafał" , 133))
print (tupleCombined) # (('Ola', 132), ('Rafał', 133))

dictConversion = dict(tupleCombined)
print (type(dictConversion)) # <class 'dict'>
print (dictConversion) # {'Ola': 132, 'Rafał': 133}

print (dictConversion["Ola"]) #132
print (dictConversion["Rafał"]) #133
print (dictConversion.values()) #dict_values([132, 133])






