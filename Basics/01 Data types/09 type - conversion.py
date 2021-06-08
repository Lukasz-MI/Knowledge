floatNum = 23.31
print (type(floatNum)) # <class 'float'>
Integer = int (floatNum)
print (Integer)   # 23
print (type(Integer)) # <class 'int'>

print (int ("32324")) #32324
print (type (int ("32324")))# <class 'int'>

IntNum = 29
floNum = float(IntNum)
print (floNum)  # 29.0
print (type(floNum)) # <class 'float'>

str1 = "234.2834"
floatNumber3 = float(str1)
print(type(floatNumber3)) #<class 'float'>
print (floatNumber3) # 234.2834

# print ("She said tha she will wait for " + 30 + " minutes" ) # TypeError: can only concatenate str (not "int") to str
print ("She said tha she will wait for " + "30" + " minutes" )
print ("She said tha she will wait for " + str(30) + " minutes" )
print ("This is my favourit number - " + str(Integer)) # This is my favourit number - 23

print ( "I like these numbers" + str((24,43,102)) ) # I like these numbers(24, 43, 102)
print ("I like these numbers" , 23.5, (34,24,32,52)) 
# I like these numbers 23.5 (34, 24, 32, 52), with comma you don't have to convert