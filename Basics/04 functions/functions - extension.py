# default arguments

def printBuyersData (name, contact = "unknown", priceRange = "below 100k", localization = "Europe"):
    print(name, "contact:", contact, "Price range:", priceRange, "Place:", localization)

printBuyersData ("Zbyszek")

printBuyersData ("Krzysztof", "Krzysztof@default.com" , "over 150k" , "USA")
printBuyersData ("Gertrude", "Gertrude@default.com") 

# named arguments

printBuyersData (priceRange = "over 150k", name = "Matt") # Matt contact: unknown Price range: over 150k Place: Europe
# contact and localization uses default data. Order can be different than in the defined function.

#arguments order

def buyersData2 (name, / , contact = "unknown", * , priceRange = "below 100k", localization = "Europe"):
    print(name, "contact:", contact, "Price range:", priceRange, "Place:", localization)

buyersData2 ("Kasia" , "Kasia@default.com" , priceRange = "over 250k" , localization = "Germany")

# name is a positional argument - it can be executed only via keyword: name = "Kasia" will return an error.

buyersData2 ("Lena" , contact = "lena@default.com", localization = "Czech Republic")
# Lena contact: lena@default.com Price range: below 100k Place: Czech Republic

# after a star you cannot give positional arguments:

def shoppingList (product , / , * ,  number):
    print (product + str(number))

# shoppingList ("eggs" , 14):
# error: shoppingList() takes 1 positional argument but 2 were given

shoppingList ("eggs " , number = 14) # eggs 14

number = 15
print ("\nTEST 1")
def testingVariable ():
    print (number)
print(number)

testingVariable () # 15

print ("\nTEST 2")

def testingVariable2 ():
    number = 7
    print(number)

testingVariable2 () # 7 -  local variable used within function

print (number) # 15 - global number used

print("\nTEST 3")

def testingVariable3 ():
    global number
    number = 20
    print(number)

testingVariable3 () # 20
print(number) # 20 - number changed in global variable to 20
testingVariable3Result = "number changed in global variable to 20 thanks to the use of keyword global within function."
print(testingVariable3Result)

print("\nTEST 4")

def testingVariable4 ():
    number = 25
    print(number) #25
    if 1==1:
        print(number) # 25
        if 2==2:
            number =40 # 40
            print(number)
    print (number) # 40
   
testingVariable4 () 
print (number) # 20  

testingVariable4Result = "Global number not affected - local variables used within function. \nEven though if instruction changes global variable. SEE: TEST 5.\nThe reason why is that if instruction was used within def function."
print(testingVariable4Result)

print("\nTEST 5")

if 7 < 10:
    number = 1000
    print(number)
    
print(number)

print("Changes to the global variable where made inside if instruction - number = 1000")

print ("\nTEST6")

print(number) # 1000

def first ():
    print(number)

first() # 1000

def second ():
    number = 9
    print(number)
    first()

second () # 9 , 1000 - local variable (9) and "first" function executed (1000 - it uses global variable)

print("\nTEST7")

def one ():
    number = 20
    print(number)
    def two ():
        print("number in function  \"two\" -" , number)
    two()

one()
print("global variable uncahnged -" , number)



