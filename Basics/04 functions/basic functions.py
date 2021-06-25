

def addNumber (a,b):
    return a + b

def minNumber (a,b):
    return a - b

def multiNumber (a,b):
    return a* b

def sevNumbers (number1, number2, number3):
    result = number1 + number2 + number3
    return result

print (sevNumbers(2,6,220)) # 228

numero = minNumber(40,23)
print(numero) # 17

numeroDuo = sevNumbers(numero, multiNumber(3, 7) , 25)
print (numeroDuo) #63

def AddNumbers3 (a,b,c):
    return a + b + c
print(AddNumbers3 (1, 4*3, 2))

def sumListElements (listData):
    if len (listData) == 0:
        print ("Empty list!")
        return None
    result = 0
    for v in listData:
        result += v 
    return result

print (sumListElements ([]))
print (sumListElements ([1,4,5,6,5,2]))

def list2 (listData):
    if len(listData) == 0:
        return
    for v in listData:
        print (v)

# there is no need to use "print" as it is incorporated in the code.

list2 ([])
list2 ([4,5,7])


#immutable def function: 

string = "hi"

def addToStr (string):
    print(id(string))
    string += "!"  # new  reference id is created.
    print(id(string))
    print (string)

addToStr(string) # hi!
addToStr(string) # hi!
addToStr(string) # hi! - each time function is executed in the same way - no modification.
print(string) # console result: hi

# mutable def function:

listData = [5,10,15,25,30]
print(id(listData)) # 2233615850560

def listOfItems (lista):
    print(id(lista)) 
    lista.append (20)
    print(id(lista))  
    print(listData)


listOfItems(listData) # [5, 10, 15, 25, 30, 20] # the same references 2233615850560 = 2233615850560
listOfItems(listData) # [5, 10, 15, 25, 30, 20, 20] # the same references 2233615850560 = 2233615850560
listOfItems(listData) # [5, 10, 15, 25, 30, 20, 20, 20] # the same references 2233615850560 = 2233615850560

# each time function listOfItems is executed the change inside a mutable data type is made.




    