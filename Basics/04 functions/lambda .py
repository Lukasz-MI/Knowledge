from functools import reduce
# lambda

suma = lambda a,b: a + b
print (suma(2,5))

result = (lambda a,b,c: ((a+b) *c))
print (result(2,8,10)) # 100 

def newLambda (number):
    return lambda f: f * number

doubler = newLambda(2) 
print (doubler(3)) # 6


# map func

listData = [0,2,4,6,8,10]
multiply = list(map (lambda a: a *3 , listData))

print(multiply) # [0, 6, 12, 18, 24, 30]

result2 = list(filter(lambda a: a < 1 , listData))
print(result2) #[0]

result3 = reduce(lambda x,y: x+ " " + y, ("Kate" , "Bogdan", "Bartek", "Josephine")) 

print (result3) # Kate Bogdan Bartek Josephine

namesList = ("Kate" , "Bogdan")
print (namesList) # ('Kate', 'Bogdan')