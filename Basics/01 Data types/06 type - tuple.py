data = tuple(("engine", "breaks", "clutch", "radiator" ))
print (data)
# data [1] = "steering wheel" # cannot be executed as tuple does not support item assignment

story = ("a man in love", "truth revealed", "choice")
scene = ("new apartment", "medium-sized city", "autumn")

book = story + scene + ("length",) # Tuple combined

print (book)
print(len(book))
print(type(book)) # <class 'tuple'>

emptyTuple = ()
print(emptyTuple)
print(type(emptyTuple)) # <class 'tuple'>

print (book [-1])
print (book [len(book) -1])

print (book [3:])
print(book[::2])

cars = (("KIA", "Hyundai", "Mazda") , ("bmw", "mercedes", "Audi"))
print(cars)
print(cars[0][0]) # second tuple, first value - KIA

if "Mazda" in cars[0]:
    print ("Yupi!") 

# del cars [0] - single element deletion not allowed

del cars

# print(cars) - whole tuple deleted - NameError: name 'cars' is not defined

tuplex3 = book * 3
print(tuplex3)