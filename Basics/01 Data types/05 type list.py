list = ["Kate", "Ralph" , 22,  "Anne" , 33]

print (len(list))   # 5
print (type(list))   # <class 'list'>
print (list)

print (list[0])

print (list[4])      
print (list [len(list)-1])
print (list[-1])
# last element printed: [4]; [5-1] = [4]; [-1]

print (list [0:])
print (list [1:4]) # 'Ralph', 22, 'Anne' - index 4 - 33 is excluded from the result in this range

del list [1]
print (list)

print (22 in list)
print (33 in list)
print ("Ralph" in list)

# Ralph is missing in the list, he was removed from it

list.insert(1, "Ralph")
print (list) # Ralph is back

if "Ralph" in list:
    print ("hoooooraah!")
    print ("Yay. He is back!")
# result = hoooooraah! Yay. He is back!

if "Jennifer" in list:
    print ("hoooooraah!")
    print ("Yay. She is here!")
# no result 

for x in list:
    print (x)

# each element from the list is represented by x and printed one after another - loop

data = [
    ["Brook", "Mat"],
    ["Bridget", "Hannah"],
    ["Monika", "Bartek"]
]

print (len(data)) # 3 =  3 lists
print(data)

print (data[2][0]) # Monika - list 3, name 1 

data1 = [3,4,5]
data2 = [1002, 1003, 1004, 1005]

fullList = data1 +  data2

print (fullList)
print (len(fullList)) #7
print (fullList [len(fullList) - 1]) # index [6] - element 7 printed







