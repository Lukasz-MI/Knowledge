#Falsy Values - values that show result "false" after conversion to boolean

print (bool(False)) # False

print (bool (0)) # False
print (bool (0.0)) # False

print (bool (())) # False
print (bool ([])) # False
print (bool ({})) # False
print (bool ("")) # False

print (bool(None)) # False

# True results:

print (bool (True))
print (bool (12))
print (bool ((11,23.12,44)))
print (bool ("Don't give in"))
print (bool (["Anne", 44, 0.78, "Kate"]))

