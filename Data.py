import math
#string data type
#literal assignment
first = "Dave"
last = "Gray"

# print(type(first))
# print(type(first) == str) 
# print(isinstance(first, str))

#constructor function
# pizza = str("Pepperoni")
# print(type(pizza))
# print(type(pizza) == str)
# print(isinstance(pizza, str))

# concatenation
fullname = first + " " + last
print(fullname)

fullname += "!"
print(fullname)

#casting a number to a string
decade = str(1980)
print(type(decade))
print(decade)

statement = "I like rock music from the " + decade + "s."
print(statement)

#Multiple lines
multiline = '''
Hey, how are you?

I was just checking in.
                              All good?

'''
print(multiline)

#Escaping Special Characters
sentence = 'I\'m back at work!\tHey!\n\nWhere\'s this at\\located?'
print(sentence)

#String Methods
#string casing

print(first)
print(first.lower())
print(first.upper())
print(first)

#replace characters/strings
print(multiline.title())
print(multiline.replace("good", "ok"))
print(multiline)

#whitespace
print(len(multiline))
multiline += "                                        "
multiline = "            " + multiline
print(len(multiline))

print(len(multiline.strip()))
print(len(multiline.lstrip()))
print(len(multiline.rstrip()))

#Build a menu
title = "menu".upper()
print(title.center(20, "="))
print("Coffee".ljust(16, ".") + "$1".rjust(4))
print("Muffin".ljust(16, ".") + "$2".rjust(4))
print("Cheesecake".ljust(16, ".") + "$4".rjust(4))

print("")

#string index values; index start at "0"
print(first[1])
print(first[-1]) #last letter in string
print(first[1:-1]) #end value won't be included
print(first[1:])

#Some methods return boolean data
print(first.startswith("D"))
print(first.endswith("Z"))

#Boolean data type
myvalue = True
x = bool(False)
print(type(x))
print(isinstance(myvalue, bool))

#Numberic data types

#integer type
price = 100
best_price = int(80)
print(type(price))
print(isinstance(best_price, int))

#float type; decimal value
gpa = 3.28
y = float(1.14)
print(type(gpa))

#complex type; used in electrical engineering
comp_value = 5+3j
print(type(comp_value))
print(comp_value.real)
print(comp_value.imag)

#Built-in functions for numbers

print(abs(gpa)) #absoulte value
print(abs(gpa * -1))
print(round(gpa)) #rounds to nearest integer
print(round(gpa, 1)) #round to "1" decimal place

# Always put "import" like import math at top of file

# *math function was imported above*
print(math.pi)
print(math.sqrt(64))
print(math.ceil(gpa))
print(math.floor(gpa))

#Casting a sting to a number
zipcode = "10001"
zip_value = int(zipcode)
print(type(zip_value))

# Error if you attempt to cast incorrect data
  #zip_value = int("New York")
