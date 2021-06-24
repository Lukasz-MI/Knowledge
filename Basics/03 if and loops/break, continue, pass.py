# break, continue, pass


data = [1, 3, 5, 7, 9]

for v in data:
    if v == 7:
        break
    print(v)  # 1, 3, 5 - loop will end when v equals 7


zoo = ("elephant" , "penguin" , "lion", "cat", "tiger") # continue

for j in zoo:
    if j == "penguin" or j == "cat": # this istruction means that when variable j = "penguin" - iteration will be omitted
        continue        
    print(j)

if 10>2:
    pass 
# - this instruction can be changed in the future by some other entry.
# the crucial thing is that code can be run in the console. If we left it blank after ":" there would be an error. 
# if 1 >0: # IndentationError: expected an indented block
