
# and

print (5>=5 and 2<4) #True
print (-4 < 2 and 1> 1.5 ) # False - both conditions have to give the "true" result  for "and" operator

taskCompleted = True
LinesofCodeWritten = 100

if taskCompleted == True and LinesofCodeWritten >=50:
    print ("go home")     

hour = 14
updatesInstalled = 2  

if taskCompleted == True and LinesofCodeWritten >= 70 and hour >= 14 and updatesInstalled >= 1:
    print ("Free to go")

# or 
print (17 >= 15 or 24 < 4) # True
print (2 >= 3 or 1 >2 ) # False - at least one condition has to be met for the summary result to be TRUE

print ( 3 != 4 or 6 < 2) # True = 3 does not equal 4

Ania = 28
Kasia = 22

if Kasia < Ania or "Jake" == "Yake":
    print ("a part is true") # True

if Ania == Kasia or 4 != 4 or 2>1 : # last value is true only
    print ("1 in third") 

print (not False) # True

print (3> 7) # False
print (not 3 > 7) # True - "not" serves as a contrary to what's stated - e.g. False becomes True 

print (Kasia == Ania or not 1 < 0) # one of the values becomes "True" and sum is renderred as True as well
print (not 4 > 5 and Kasia != Ania) # both elements are considered "True"
print (not 4 > 2 or 4 <= 7 ) # True - the second element is "True"

taskCompleted = False

if taskCompleted == True:
    print ("go home")

if not taskCompleted:
    print("stay a bit longer if you can")
