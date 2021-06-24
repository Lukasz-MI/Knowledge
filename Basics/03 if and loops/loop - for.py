# It is used for lists, tuples, sets, dictionaries, strings

listData = [1,2,3,4,5,6,7]

for v in listData: # v stands for 1 and then for every other number. Other iterations are performed in the loop until the last entry in the list - 7.
    print(v)

tupleData = ("Ona" , "lubi" , "jabłka")

for f in tupleData:
    print(f)

dictionaryData = {"Kate" : 30 , "Anne" :23}

for h in dictionaryData:     # h - stands for the first key and then for all of the remaining keys in the dictionary.
    print (dictionaryData[h]) # 30, 23 - [h] - shows values stored under keys 

for key, values in dictionaryData.items():
    print(key +" " + str(values)) # both keys and values displayed in the console - e.g. Kate 30


strData = "Matrix Inc."

for s in strData:
        print(s) 
else:
    print("loop ends here!")
    
    
    ''' results printed:
                M
                a
                t
                r
                i
                x

                I
                n
                c
                .
                loop ends here!'''

for f in {str(2) , "banana" , "quantity" , str(58)}: # Random iterations in sets
    print (f)


for b in ["Kate" , "Matt" , 25, "years together"]:
    print (b) 
# loop for in with range
for v in range(4):
    print(v)
for v in range (2,10):
    print(v)
for v in range (2,11,2):
    print(v)