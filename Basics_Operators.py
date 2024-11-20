#!/bin/python3

#Print string
"""print("Strings and things")
print("Hello World")
print("""""")
print("This is a" + " string" )

print("\n") #new line

#Math
print("Math time")
print(50+50) #add
print(50-50) #subtract
print(50*50) #multiply
print(50/50) #divide
print(50**2) #exponents
print(50%6) #modulo or mod
print(50 // 6) #number without leftovers"""

#Variables & Methods

quote = "All is fair"
print(len(quote))
print(quote.upper()) #uppercase
print(quote.lower()) #lowercase
print(quote.title()) #title

name = "Heath"
age = 29 #int(29)
gpa = 3.7 #float(3.7)
print(int(age))
print(int(29.9))
print("My name is " + name + " and I am " + str(age) + " years old.") #have to convert int(age) to "str" in order to print!
age += 1
print(age)

birthday = 1
age += birthday
print(age)

#functions
print("Now, some functions;")
def who_am_i(): #things inside the function only exist in the function, notice how "name" didn't replace the one outside the funtion
  name = "Heck"
  age = 29
  print("My name is " + name + " and I am " + str(age) + " years old.")
who_am_i()
print("name: " + name)

#adding parameters
def add_one_hundred(num):
  print(num+100)
add_one_hundred(100)

#add in multiple parameters
def add(x, y):
  print(x+y)
add(7, 7)

#using "return"
def multiply(x, y):
  return x*y
print(multiply(7, 7))

def square_root(x):
  return x**.5
print(square_root(64))

def nl(): #new line
  print("\n") 

nl()

#boolean expressions (True or False)

print("""Boolean expressions: 
#If expression is true then boolean returns true
#If expression is false then boolean returns false""")

nl()

bool1 = True
bool2 = 3*3==9
bool3 = False
bool4 = 3*3 != 9

print(bool1, bool2, bool3, bool4)
print(type(bool1))
bool5 = "True" #string
print(type(bool5))
nl()

#Relational and Boolean Operators
