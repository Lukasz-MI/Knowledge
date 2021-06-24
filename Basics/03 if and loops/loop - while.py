number = 7

while number > 0:
    print (number)
    number = number - 1 # lopp will run through all instances of number - 1 as long as number > 0
    if number == 0:
        print ("loop is over") # loop is over as number equals 0 and does not meet loop condition

''' Results:
    7
    6
    5
    4
    3
    2
    1
    loop is over '''

num = 5

while (True):
    print ("Enter a number in the console to add to the previous result or type in exit to stop the loop. \nThe inital value equals 5")
    strData = input()
    if(strData == "exit") :break
    num += int(strData)
    print("New value after adding " + str(strData) + " is " + str(num))

number2 = 5

#while and else

while number2 < 23 :
    print(number2)
    number2 += 3
else:
    print("end of the lopp!") # end of the lopp!

    