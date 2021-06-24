num = 0
operation = None
reset = True
result = None
calcOperations = ["+" , "-" , "*" , "/", "**"]

while True:
    if reset == True:
        num = int (input("Give the first number:"))
        reset = False # reset = False - allows for continuation of operations in calculator.

    operation = input ("Use symbol: +, - * , / , ** " + " or use exit if you want to quit or reset if you want to start over:")
    if operation == "exit":
        break
    if operation == "reset":
        reset = True
        continue
    if not operation in calcOperations:
        print("incorrect input")
        continue
    

    secondNum = int(input("add a number:"))

    if operation == "+":
        result = num + secondNum
    if operation == "-":
        result = num - secondNum
    if operation == "*":
        result = num * secondNum
    if operation == "/":
        result = num / secondNum
    if operation == "**":
        result = num ** secondNum

    print ("Result: " + str(num) + " " + operation + " " + str(secondNum) + " = " + str(result))

    num = result
    result = None

