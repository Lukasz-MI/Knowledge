# if - each condition is introduced by another indent

num = 24

if num >10:
    print ("higher than 10")
    if num > 20:
        print (str(num) + " - higher than 20 also")
        print ("let's see if there is more")
        if num > 24:
            print (str(num) + " - higher or equal 24") # the condition is not met
            if num > 22:
                print(str(num) + " - higher than 22") # the code "stopped" in the previous line and does not account for the below "True" result.
    

print ("results provided")


''' if and elif - The code is "stopped" where the condition is met. With "if" it is different - each
line of code is checked: '''

if num == 20:
    print ("It does equal 20!")
elif num == 24:
    print("Number is equal 24") # Number is equal 24
elif num >= 24:
    print ("higher or equal 24") # This result is also True, but it won't be shown

if num == 24:
    print("24 = 24") # 24 = 24
if num > 10:
    print ("More than 10") # More than 10

# if elif and else
num2 = 27

if num2 > 30:
    print ("more than 30")
elif num2 == 30:
    print("num2 equals 30")
else:
    print ("no match found")    # no match found

if 6 > 4: print("6 is more!") # 6 is more!
