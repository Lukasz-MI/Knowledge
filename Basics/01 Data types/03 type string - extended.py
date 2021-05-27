onlyOne = "God "

print (onlyOne [0])
print (onlyOne [1])
print (onlyOne [2])

print (onlyOne [0:3])

print (onlyOne *3 ) # printing single signs, selected combination of signs, repeating" 

text = '''When 
I need
You ''' 

print (text) # several lines of text printed

text = "When\nI need\nYou\nI just close\nmy eyes\nand I'm with\t You" 

print (text) # several lines of text printed - other method

motto = "You'll never walk alone" 

print (motto) 

""" apostrophe printing to avoid the syntax error thanks to the use of "":
'You'll never walk alone' - would not work as a string of text """

motto2 = ' I won\'t give up on you' 

print (motto2) # apostrophe printing to avoide an error in syntax thank to the use of \

print (len(motto2)) # number of signs in motto2

mottoCombined = motto + "." + motto2 + "."

print (mottoCombined)

print (mottoCombined [7:])  

""" from sign number 8 until the end
(8th sign = [7]: [0 - y ,1- o,2 - u, 3 - ',4 - l,5 - l ,6 - space ,7 - n]"""

print (mottoCombined [7])

print (mottoCombined [::2]) # print every 2nd sign, but starting from the first letter - letter 1, letter 3, letter 5...



