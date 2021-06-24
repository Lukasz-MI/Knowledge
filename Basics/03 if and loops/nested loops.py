from typing import List


severalLists = [
["Kate" , "John" , "Adam"],
[23, 80, 122],
["banjo" , 1 , "guitar" , 2 , "vocals " , 3]
]

print(severalLists)

for list in severalLists:
    for v in list:
        print (v)