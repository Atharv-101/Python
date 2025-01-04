#Comments in Python

# This is Single Line Comment

"""
Multi Line Comment
"""
from platform import python_version

"""
Comments in Python are used to explain code, improve readability,
and aid in debugging,but they are ignored during execution.

"""

"""

Python Character Set
Letters – A to Z, a to z
Digits – 0 to 9
Special Symbols - + - * / etc.
Whitespaces – Blank Space, tab, carriage return, newline, formfeed
Other characters – Python can process all ASCII and Unicode characters as part of data or literals

"""

print("Hello World")

print("This is Hello world with double quote")    #print function is used to print or display codes on output screen
print('This is Hello world with single quote')          #when ever we use print we can use any of this "" or ''

print("I'm fist file of python","Developed by Atharv\n")

print(20)       #here we have printed 20
print(20+30)    #in this case we have directly add without and diff function
print('*' * 10)
# here we have used * to multiply we can use other arithmetic operators

#Variables : it is a name given to a Memory location in a program

name="Atharv"
age=20
python_version=3.11

print("My name is ",name)
print("My age is", age)
print("Currently I'm using Python version\n", python_version)         #here we have saved Variables and called them according to our need

# Let's see use of arithmetic operators
print("Let's see use of arithmetic operators\n")            #"\n" is used to change the line or Next line
a = 1000
b = 500
add = a+b
sub = a-b
mult = a*b
div = a/b

print("Add of two numbers is", add)
print("Sub of two Numbers is", sub)
print("Mult of two Numbers is", mult)
print("Div of two Numbers is", div)

#Type Conversion
print("\nType Conversion")      #It is used to Convert one datatype in another datatype

c = 2       #int
d = 4.25    #Float
sum = c+d
print("here is sum of two diff datatypes",sum)



#Input in Python
print("\n Input in Python")
"""
    Syntax
    input(prompt)
"""
input("How are you: ")

name = input("Enter Your name:")
print("Welcome",name)