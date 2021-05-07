'''
 Python 3 - Quick Beginner Code-Sheet Examples (originally made for Mansour "my son", or for anyone would like to learn Python 3 - quickly in <= 24 hours
 Doha - April 27, 2021
 Using Python 3.7.3 interpreter
 version: 1.4 (last update on May 6, 2021)
 IDE code editor: Thonny v3.3.6, to see other IDE for Python, read this: https://realpython.com/python-ides-code-editors-guide/
 
 This is one Python3 source code-file: full of basic knowledge to start and learn easily the Python3 langugae (beginner level until intermediate level with simple coding examples)
 
 When finishing this quick-rush beginner Python code examples, then you can dive more deep into these tutorials - mentioned here below:
 
> https://www.w3schools.com/python/ (I think the best Python 3 resource available online)

> https://realpython.com/ (I learned a lot from them...real experts in Python 3)

> https://www.learnpython.org/ (you can run the code online and try-it with many examples).

> 99 basic Python 3 examples from zero to intermediate level:
 https://www.programiz.com/python-programming/examples

> 26 Python 3 examples from beginner to intermediate level:
 https://skillcrush.com/blog/python-programming-examples/
 
> 100 of Python 3 excercises for Intermediate to Expert level:
https://www.w3resource.com/python-exercises/

Also there are excellent Python 3 modules and important to know, like: Numpy, Pandas, Matplotlib, TkInter, Scipy, TensorFlow, PyGame, PyQT, Flask, Web2Py, Kivy, etc.
'''

# Please visit each section commented with many #### in sequence, as it is written step by step to learn:

'''
 Python programming language definition from: https://en.wikipedia.org/wiki/Python_(programming_language)
 
 Python is an interpreted high-level general-purpose programming language. Python's design philosophy emphasizes code readability with its notable use of significant indentation.
 Its language constructs as well as its object-oriented approach aim to help programmers write clear, logical code for small and large-scale projects.
 
 Guido van Rossum (founder and creator of this language: Thank you) began working on Python in the late 1980s, as a successor to the ABC programming language,
 and first released it in 1991 as Python 0.9.0, then Python 2.0 was released in 2000 and introduced new features, then Python 3.0 was released in 2008 and was a major revision
 of the language that is not completely backward-compatible and much Python 2 code does not run unmodified on Python 3.
'''

# This is how we define int data type (integer number variables), variable in programming/coding means a temporary storage for a value to use during coding your logic:
int_pos_number_variable = 10
int_neg_number_variable = -10
# print(int_number_variable) ## just to show you how to comment a single line

# This is how we define float/decimal data type (float number variables):
dec_pos_number_variable = 10.5
dec_neg_number_variable = -10.25

# We call it in programming: Boolean data type (True/False)
true_variable = True 
false_variable = False

# How to define a list of int items or string items like calendar days or week numbers, etc.:
# Python list are changable  --> mutable: you add to it, update it or delete it:
list1_int = [1, 2, 3, 4, 5, 6, 7] # we have 7 days in a week
list2_str = ['Mon', 'Tue', 'Wed', 'Thur', 'Fri', 'Sat', 'Sun']
list3_empty = [] # empty list

print('##################################################################################')

# This is how we define a string or free text --> String data type can be defined with single-quote, double-quotes or three-quotes
my_name_string = "I am Michael Jackson"
my_goal_string = "and would like to learn the basics of Python language!"

my_str = '''!!Waw!!''' # I don't like it personally to do that!!

# basic keyword/built-in function to print/show results to ouput (i.e. Shell, console output or terminal screen)
print(my_name_string)
print(my_goal_string)
print(my_str)
print(list1_int)
print(list2_str)
print('Empty list:', list3_empty)

# My favourite function or method in Python and really powerful stuff --> sort()
print('List of days before soting:', list2_str)
list2_str.sort() # Ascending order sorting by default and this method does not return any value; it simply sorts the contents of the given list
print('List of days after sorting:', list2_str)

# Now sort your list in descending or reverse order, just use the parameter named 'reverse':
list2_str.sort(reverse=True) # Descending order sorting
print('List of days after reverse sorting:', list2_str)
print('##################################################################################')

# Put and merge all strings into one line of statement --> this is called in Programming: String Concatenation:
print(my_name_string + ', ' + my_goal_string)
# Use of terminal new line character '\n'
print(my_name_string + ',\n' + my_goal_string)

# Use of String replication trick in Python3 --> x number display my string or just simply repeat it
print(5 * 'Mohi\n')

# IMPORTANT NOTE: You cannot merge or concatenate (+) an int data type with string data type, otherwise Python will reject it with Exception
#  (TypeError) as below <Uncomment the code-line below and see the exception alert>:
# print('Python' + 3) # it will throw a runtime exception called TypeError

print('##################################################################################')

# MATH operators for daily language use:
# Addition (+):
print('+: ', 10 + 10)

# Substraction (-):
print('-: ', 10 - 10)

# Multiplication (*):
print('*: ', 10 * 10)

# Division (/):
print('/: ', 8 / 2) # always return a float/decimal number data type

# Exponent (**):
print('**: ', 2 ** 8) # like 2 to power of 6

# Integer Division (//):
print('//: ', 8 // 2) # always return an int data type

# MOD or reminder in programming (%) - this is not percentage as in normal speaking language:
print('Mod: ', 8 % 2) # always return a float/decimal number

print('##################################################################################')

# Output formatting tricks using print():
print(1, 2, 3, 4)
print(1, 2, 3, 4, sep='*') # now separator now is not space but anything you like: -, *, (), ...
print(1, 2, 3, 4, sep='#', end='&') # end of string line, put an end character...fun!

print() # put an empty line

print('##################################################################################')

# Another good built-int function like input():
neved = input('What is your name? ')
print('A neved akkor: ', neved)

# Check this trick: how to convert a string data type to int data type:
korod = int(input('How old are you? '))
print('A korod akkor: ', korod)

if(korod == 18):
    print('You can watch porn movies alone!!')
else:
    print('You canNOT watch porn movies alone!!')

print('##################################################################################')

# How to know the length of String, any data-structure like list: len() function - built-in function and very important in programming:
# Since Python 3.6 introduced a flexible style to display your variables, functions, expressions, objects using F-String concept like below --> put f'' at the print() function:

# Basic Python3 formatting:
print(f'Length of your name ({neved}) is {len(neved)}')
print(f'Length of your List ({list2_str}) is {len(list2_str)}')

print('##################################################################################')

# Output formatting especially for displaying floating/decimal numbers or Hex numbers --> f-string format floats
#  very good resources for this F-String formatting with detailed examples: https://zetcode.com/python/fstring/, https://mkaz.blog/code/python-string-format-cookbook/#f-strings)
'''
%.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.

%x/%X - Integers in hex representation (lowercase/uppercase)
'''
no_var = 102342.344433340000
print(f'Decimal number formatting in Python (2 decimal digits example): {no_var:.2f}') # :.2f means 2 decimal digits
print(f'Decimal number formatting in Python (5 decimal digits example): {no_var:.5f}') # :.5f means 5 decimal digits

int_var = 450
print(f'Hex number formatting in Python (displaying small-letters Hex-Number example): {int_var:x}') # :x means display hexadecimal number in small letters
print(f'Hex number formatting in Python (displaying capital-letters Hex-Number example): {int_var:X}') # :x means display hexadecimal number in capital letters

print('##################################################################################')

'''
Source: https://www.w3schools.com/python/python_ref_string.asp:

String has many popular functions and at least you have to be familiar with at least 8-12 functions to be aware of, as string formatting and handling will be 8% of your daily coding

Method/Function   Description
capitalize()      Converts the first character to upper case
casefold()        Converts string into lower case
center()          Returns a centered string
count()           Returns the number of times a specified value occurs in a string
encode()          Returns an encoded version of the string
endswith()        Returns true if the string ends with the specified value
expandtabs()      Sets the tab size of the string
find()            Searches the string for a specified value and returns the position of where it was found
format()          Formats specified values in a string
format_map()      Formats specified values in a string
index()           Searches the string for a specified value and returns the position of where it was found
isalnum()         Returns True if all characters in the string are alphanumeric
isalpha()         Returns True if all characters in the string are in the alphabet
isdecimal()       Returns True if all characters in the string are decimals
isdigit()         Returns True if all characters in the string are digits
isidentifier()    Returns True if the string is an identifier
islower()         Returns True if all characters in the string are lower case
isnumeric()       Returns True if all characters in the string are numeric
isprintable()     Returns True if all characters in the string are printable
isspace()         Returns True if all characters in the string are whitespaces
istitle()         Returns True if the string follows the rules of a title
isupper()         Returns True if all characters in the string are upper case
join()            Joins the elements of an iterable to the end of the string
ljust()           Returns a left justified version of the string
lower()           Converts a string into lower case
lstrip()          Returns a left trim version of the string
maketrans()       Returns a translation table to be used in translations
partition()       Returns a tuple where the string is parted into three parts
replace()         Returns a string where a specified value is replaced with a specified value
rfind()           Searches the string for a specified value and returns the last position of where it was found
rindex()          Searches the string for a specified value and returns the last position of where it was found
rjust()           Returns a right justified version of the string
rpartition()      Returns a tuple where the string is parted into three parts
rsplit()          Splits the string at the specified separator, and returns a list
rstrip()          Returns a right trim version of the string
split()           Splits the string at the specified separator, and returns a list
splitlines()      Splits the string at line breaks and returns a list
startswith()      Returns true if the string starts with the specified value
strip()           Returns a trimmed version of the string
swapcase()        Swaps cases, lower case becomes upper case and vice versa
title()           Converts the first character of each word to upper case
upper()           Converts a string into upper case
zfill()           Fills the string with a specified number of 0 values at the beginning
'''

print('String function usage like upper(): ', neved.upper())
str_text = "Love apples, apple are my favorite fruit!"
x = str_text.count("apple")
print('String function usage like count(): ', x)

'''
Example: https://www.w3schools.com/python/ref_string_partition.asp
Search for the word "bananas", and return a tuple with three elements:

1 - everything before the "match"
2 - the "match"
3 - everything after the "match"
'''
txt = "I could eat bananas all day"
x = txt.partition("bananas")
print(x)

print('##################################################################################')

# Back to list data-structure and most important methods/functions will come always to you in handy:
# Let us suppose you have a list and need to change it or update it's items, then how?

# direct way to update an existing item/element value in the list of yours:
list1_int[len(list1_int)-1] = 8
print('Printing int list elements to see it again after updating one item at the end:', list1_int)

# Other professional way to use list available methods like: append() or insert():
list1_int.append(9)
print('List of int days after using append():', list1_int)

list1_int.insert(6, 7) # insert(index or position you wish to insert, value wish to add)
print('List of int days after using insert():', list1_int)
list1_int.insert(7, 8) # insert(index or position you wish to insert, value wish to add)
print('List of int days after using insert():', list1_int)

# Waw: now we have duplicate items in our list, let us use another way to remove an item, hence use list method called: remove()
list1_int.remove(8) # search for duplicated value and remove it from your list
print('List of int days after using remove():', list1_int)

# or use pop() function as it will remove the last item in the list
list1_int.pop()
print('List of int days after using pop():', list1_int)

# or you wish to empty or delete all items in the list --> empty it or just remove it from OS Python memory --> erase it, or scrap it:
del list1_int
# Uncomment below line and Python Exception will occur called: NameError: name 'list1_int' is not defined
#print('Length of my int list after using del keyword/command:', len(list1_int))
print('##################################################################################')

# How to define a function and calling a function --> Python language main essential strong perspective: how to define an action and to re-use it multiple times as per my code logic:
# Example: define a function to calculate square root or math sin() calculation, etc.

def calcSquareRootFunction (myParameter):
    return (myParameter * myParameter)

# Now call it and use it:
print("Using my own function named calcSquareRootFunction(): ", calcSquareRootFunction(1))
print("Using my own function named calcSquareRootFunction(): ", calcSquareRootFunction(10))
print("Using my own function named calcSquareRootFunction(): ", calcSquareRootFunction(100))
print("Using my own function named calcSquareRootFunction(): ", calcSquareRootFunction(1000))
print("Using my own function named calcSquareRootFunction(): ", calcSquareRootFunction(10000))

print()

# Another interesting customized functions to define, like convert from KM to Miles:

km_value = 10 # 10 km

def km2Mile(kmParameter):
    # calculate miles from given KM unit value:
    # conversion factor
    conv_fac = 0.621371 # constant
    return (kmParameter * conv_fac)

print(f'{km_value} kilometers is equal to: {km2Mile(km_value)} miles!')

print()

# #### More examples of functions usage:

# Calculate from Celsius temperature to Fahrenheit:
def celsiusToFahrenheit(celsiusParam):
    # formula to F: (C × 9/5) + 32
    return (celsiusParam * 1.8) + 32

celsius_value = 48 # 48C 
print(f'{celsius_value}C Celsius to Fahrenheit temperature conversion: {celsiusToFahrenheit(celsius_value)}F degree Fahrenheit')

print()

# How to calculate a light year: original article from: https://www.wikihow.com/Calculate-a-Light-Year
#  Light years are actually a measure of distance that uses light as a standard (i.e. how far light travels in one Earth year), but not time like calculating the distance in km or miles.
#  The formula looks like this: the actual distance of a light year: need to multiply the speed of light by the number of seconds in a year.
#  So we can say Distance of light (d) = Speed of light (c) x (one year --> total number of seconds in one year --> t)
#  hence our function will be in Python like this:

# Calculate distance of light year:
def calcDistinceOfLightYear():
    # Define the speed of light. Light in a vacuum travels at a velocity of 299,792 kilometers per second
    speed_of_light = 299.792 # in km
    # Calculate the number of seconds in a year: you will do a series of multiplications by conversions units, which is convert years to seconds you will multiply the number of days in a year times the number of
    #  hours in a day, times the number of minutes in an hour, times the number of seconds in a minute:
    tota_seconds_in_one_year = 365 * 24 * 60 * 60 # approx 31.536.000 seconds
    
    return speed_of_light * tota_seconds_in_one_year

print(f'Distance of a light year: {calcDistinceOfLightYear()} trillion km')

print()

# Calculate Area of Triangle (Heron’s Formula, original source: https://byjus.com/maths/area-of-a-triangle/
def calcAreaOfTriangle(side1, side2, side3):
    # 1st we need to calculate the semi perimeter of a triangle: is the distance covered around the triangle and is calculated by adding all the three sides of a triangle diving it by 2:
    semi_perimeter = (side1 + side2 + side3) / 2
    
    # 2nd use Herons's equation to finally get the area of triangle:
    return (semi_perimeter * (semi_perimeter - side1) * (semi_perimeter - side2) * (semi_perimeter - side3)) ** 0.5

print(f'Area of Triangle based on Heron formula (calcAreaOfTriangle(5, 6, 7)) is: {calcAreaOfTriangle(5, 6, 7)}')

print('##################################################################################')

# Random number generator: very famous and used in coding almost in each project, why not to learn it now:

# Example: Program to generate a random number between 0 and 9

# importing the random module/library
import random

print(random.randint(0,9)) # randint(): will return an int number not decimal or float --> random number generated can be duplicated also, for example: 1, 1, 4, 6, ...

'''
Python Documentation says for randint() usage:

random.randint(a,b)
This returns a number N in the inclusive range [a,b], meaning a <= N <= b, where the endpoints are included in the range.
'''

print('##################################################################################')

# Using loops: essential programming technique and programmer cannot survive a code without it:

# Example: put above random int generator into a loop from 1 to 10:
for index in range(1, 11):
    print(f'For loop current index[{index}]', random.randint(0,9))

# Now loop thru a list
counter = 0
for element in list2_str:
    print(f'Looping thru a list elements: current index[{counter}]', element)
    counter += 1
    
# Write above loop in another way using range() style: example range(1, 10): means int range will start from 1 until 9:
for xxx in range(0, len(list2_str)):
    print(f'Looping thru a list elements (range usage): current index[{xxx}]', list2_str[xxx])

print('##################################################################################')

# Since we are now starting to understand then range(), there is another good usage called "Slice a list using range style", how?
example_list1 = [23, 100, 1000, 2, 8, 10, 0]
# now for my code logic I need only the first three or four elements from above list called: example_list1, then how to do that?
print('Using slice list technique and range usage again, my original list:', example_list1)
print('Using slice list technique and range usage again, after slice:', example_list1[0:4])

print('##################################################################################')

# working with list copy (clones), really good trick in Python and does not exists in other programming languages like Java, C#:
# Example: I have an original list like: list of important items, but in the code logic I would like to work with a copy but touching original list, how to do that?

eco_cars_list = ['Ford', 'Toyota', 'Citroen']
print(f'Original cars list [ECO]: {eco_cars_list}')

# Shallow Copy technique in Python: to read more about it, here an excellent technical article: https://www.geeksforgeeks.org/copy-python-deep-copy-shallow-copy/

expensive_cars_list = eco_cars_list.copy() # clone or make a copy from original list now and play with the cloned list:
# Now remove ECO cars and put expensive ones just to make a real-life example:

expensive_cars_list.pop()
expensive_cars_list.remove('Ford')
expensive_cars_list[0] = 'Porsche'
expensive_cars_list.append('BMW')
expensive_cars_list.append('Lexus')
print(f'Original cars list [ECO] - after updating the cloned list - original is intacted: {eco_cars_list}')
print(f'Expensive cars list [Luxury]: {expensive_cars_list}')

'''
More concepts notes about: Copy a List
You cannot copy a list simply by typing list2 = list1, because: list2 will only be a reference to list1, and changes made in list1 will automatically also be made in list2.

There are ways to make a copy:

1) one way is to use the built-in List method copy().

2) Another way to make a copy is to use the built-in method list() constructor
'''
print('##################################################################################')

# Dealing with different if statements (conditional statements in Python):
'''
Just like other programming languages C, C++, Java, C#: Python supports the basic logical conditions:
 Equals: a == b
 Not Equals: a != b
 Less than: a < b
 Less than or equal to a <= b
 Greater than: a > b
 Greater than or equal to: a >= b
'''

if (10 > 1):
    print('(10 > 1) is True!')
    
if (10 < 1):
    print('Not true')
elif (10 > 1): # elif tell Python to try another if condition if the previous one(s) was not true
    print('(10 < 1) is Not True!')
    
# combine if-else-elif keywords in a logic coding style:
# Example to learn from:
age = 19
ticket_price_euro_basic = 50

if (age < 11):
    ticket_price_euro_basic = 10
elif (age >= 12 and age <= 18):
    ticket_price_euro_basic = 20
else:
    ticket_price_euro_basic = 50 # adult price > 18 years old
    
print(f'Opera concert ticket price in Euro now (based on age of {age}): ', ticket_price_euro_basic)

# Using NOT keyword: will do the opposite meaning of True:
# Example:

given_list1 = [0, 100, 20000]
test_value = -1

if test_value not in given_list1:
    print(f'Your given list: {given_list1}\n and provided test value {test_value}, is NOT in the list!')

print('##################################################################################')

# While loops (another type of loops): enable developer to run/execute a set of coding statements, as long the triggering condition is true and the loop will continue to run:

# Example:

value = 1
while (value <= 10):
    print(f'While loop, current value {value}')
    value += 1
    
# How to break/stop a loop from continue to run for any Python type of loop

# Examples:

for index1 in range(1, 11):
    print(f'Break a for loop, current index [{index1}]')
    if (index1 == 5):
        break;

value = 1
while (value <= 10):
    print(f'Break a While loop, current value {value}')
    if (value == 5):
        break
    value += 1
    
# How to make an infinite loop that running forever (i.e. used in some coding logic: like awaiting end-user input until he type the 'exist' keyword, linux terminals uses this techniques):

# !!! Becareful when using this infinite while loop !!!
counter = 1

while True:
    print('Printing this text one-line in an infinite while loop.....')
    # we need to put a break, otherwise your OUTPUT will print that text forever:
    if (counter == 20):
        break
    else:
        counter += 1
print('##################################################################################')

# One of greatest powerful feature in Python is: List comprenhensions, means: creating/generating lists data type (data-structure) based on existing lists. This powerful feature currently exists in Python (one single line of code):
# rule like this: list_variable = [x for x in iterable with or without if condition]

# Example:
list_comprehension1 = [index for index in range(10)] # generate a list of int numbers only from 0 until 9
print(f'List comprehension #1: {list_comprehension1}')

list_comprehension2 = [index for index in range(11) if index % 2 == 0] # generate a list of even numbers only, loop will go from range 0 until 10
print(f'List comprehension #2: {list_comprehension2}')

list_comprehension3 = [index ** 2 for index in range(11) if index % 2 == 0] # generate a list of even numbers with power exponent of two only, loop will go from range 0 until 10
print(f'List comprehension #3: {list_comprehension3}')

print('##################################################################################')

# Python math module/library has a vast mathmetical functions, really better than in any other languages like C# or Java, here we will examine most common ones:
import math as m # "as" means alias name to the imported Python module/library and also a reference how to use it in your code:

'''
Syntax:
math.sqrt(x)

Parameter: 
x is any number such that x>=0
'''

print('Usage of math.sqrt() function - m.sqrt(0): ', m.sqrt(0))
print('Usage of math.sqrt() function - m.sqrt(4): ', m.sqrt(4))
print('##################################################################################')

# math.pow()    Returns the value of x to the power of y

#Return the value of 9 raised to the power of 3
print('Usage of math.pow() function - m.pow(9, 3): ', m.pow(9, 3))
print('Usage of math.pow() function - m.pow(1, 2): ', m.pow(1, 2))
print('Usage of math.pow() function - m.pow(10, 10): ', m.pow(10, 10))

print('##################################################################################')

# math.factorial()  Returns the factorial of a number

print('Usage of math.factorial() function - m.factorial(0): ', m.factorial(0))
print('Usage of math.factorial() function - m.factorial(1): ', m.factorial(1))
print('Usage of math.factorial() function - m.factorial(2): ', m.factorial(2))
print('Usage of math.factorial() function - m.factorial(3): ', m.factorial(3))
print('Usage of math.factorial() function - m.factorial(10): ', m.factorial(10)) # becareful here, as factorial of very large number will depends on GPU hardware and of course power of your machine!
print('Usage of math.factorial() function - m.factorial(100): ', m.factorial(100)) # becareful here, as factorial of very large number will depends on GPU hardware and of course power of your machine!

print('##################################################################################')

'''
math.ceil(x)

Parameter: 
x-numeric expression. 

Returns: 
Largest integer greater than x.
'''
f1 = 10.1
f2 = -23.5
f3 = 10.5
f4 = 10.6
f5 = -23.1
f6 = -23.7

print('Using math.ceil() function: ')
print(m.ceil(f1)) # will be 11
print(m.ceil(f3)) # will be 11
print(m.ceil(f4)) # will be 11
print(m.ceil(f2)) # will be -23
print(m.ceil(f5)) # will be -23
print(m.ceil(f6)) # will be -23

'''
OUTPUT
11
11
11
-23
-23
-23
'''

print('##################################################################################')

'''
math.floor(x)

Parameter: 
x-numeric expression. 

Returns: 
largest integer not greater than x.
'''
f1 = 10.1
f2 = -23.5
f3 = 10.5
f4 = 10.6
f5 = -23.1
f6 = -23.7

print('Using math.floor() function: ')
print(m.floor(f1)) # will be 10
print(m.floor(f3)) # will be 10
print(m.floor(f4)) # will be 10
print(m.floor(f2)) # will be -24
print(m.floor(f5)) # will be -24
print(m.floor(f6)) # will be -24

'''
OUTPUT
10
10
10
-24
-24
-24
'''

print('##################################################################################')

# I/O file operations like reading a text file or writing data (int, string, boolean, decimal, text, etc) to a text file, is really is the most easiest coding style that Python language has! Even better than in Java or in C#:

# Example: text file reading and writing, simple text file handling --> using 'with' keyword:

list_of_greeting_strings = ['Hogy vagy vilag?\n',
                               'Hogy vagy csaladom?\n'
                               'Hol vagytok?\n']
text_file_name = 'greetings_words_text_file.txt'

# 'w': means writing mode, if text file already exists, it will be overwritten:
with open(text_file_name, 'w') as output_file1:
    output_file1.writelines(list_of_greeting_strings)
    # output_file1.close() # with keyword in Python: automatically closes the text file handler
    print(f'File Input/Output handling (I/O): creating a new text file and writing some data to it....text file named is: {text_file_name}')
    
# !!! Important to note here, that file method called .writelines() by default does not append to end of line the \n, so you need to add it in your coding --> .writelines() file method does not by default append a new line!!!

# The same way of handling text file writing, you can also do the same thing with text file-reading, as below:

# 'r': means reading mode, if text file already exists, it will be opened for reading, if does not exists then exception will be thrown to end-user: FileNotFoundError --> [Errno 2] No such file or directory: 'greetings_words_text_file.txt'
with open(text_file_name, 'r') as output_file1:
    list_of_greeting_strings = output_file1.readlines() # return a list of lines (list of strings):
    # output_file1.close() # with keyword in Python: automatically closes the text file handler
    print(f'File Input/Output handling (I/O): reading an existing text file....readed data are:')
    print(list_of_greeting_strings)
print('##################################################################################')

# If you would like to know about your current OS system and querying some info, like operating system name, type, etc., simply use the Python module/library called: platform
# Different values will appear, for example: if you running it under Ms-Windows 10, MacOS Catalina v10 or under Linux operating systems:

import platform as pm

print('Current operating system: ', pm.system())
print('Current architecture: ', pm.architecture())
print('Current machine: ', pm.machine())
print('Current OS version: ', pm.version())
print('Current processor: ', pm.processor())
print('Current Python build: ', pm.python_build())
print('Current Python compiler: ', pm.python_compiler())
print('Current Python version: ', pm.python_version())
print('Current Linux UNAME: ', pm.uname())
print('Current Linux core release: ', pm.release())

print('##################################################################################')

# Since we can now handle text files, how about CSV (Comma-Separated-Value) files?

'''
 Reading Data From a CSV File example
 You need to use build library called csv and function named 'reader()'
 This uses TAB delimiter to read the file
'''

import os # important library to deal with operating system variables or information like current folder path, file copy or folder creation, etc.
import csv

path = './.' # current folder, where this Python source code file will be read
csvFileName2read = 'test_csv_tab_delimiter.csv'

with open(os.path.join(path, csvFileName2read)) as csvFileRef:
    csv_reader = csv.reader(csvFileRef, delimiter = '\t')

    csvRowCounter = 0

    for csvRow in csv_reader:
        print(csvRow)
        csvRowCounter += 1

    print('Total CSV file line numbers: ', csvRowCounter)
# CSV file close object will be done automatically by with keyword
print('##################################################################################')

# Coming back to important data-structure definition in IT or programming, to put it as simple as possible:
#  a data structure is a collection of data values, where specific operations/actions can be applied to these data, for example: sorting, adding to it like insert, update it, or deleting it.
#  Python has another important data structure types like Tuple or Dictionary, not just list. I really like Python list, better that Arrays in Java, so let us examine these two other types:

# Tuples are unchangeable (read-only list), so you cannot remove items from it, but you can delete the tuple completely --> they are saying tuple speed is faster than list, but that another topic!
# Example:

thistuple = ("apple", "banana", "cherry")
print('Tuple (another Python data-structure type) example: ', thistuple)
del thistuple

# Uncomment this line of code and you can see Python exception: NameError: name 'thistuple' is not defined
#print(thistuple) #this will raise an error because the tuple no longer exists

# Another example of Tuple to slice them like list
another_tuple = (1, 2, 3, 4, 5, 6, 7, 8) # once Tuple is defined: you cannot add new items to it or change it!
# slice it like in list using range feature:
sliced_tuple = another_tuple[0:5]
print('Sliced Tuple example: ', sliced_tuple)

# more tricky slicing tuple example:
another_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14) # once Tuple is defined: you cannot add new items to it or change it!
sliced_tuple = another_tuple[1:12:2] # return only the 2nd element
print('Sliced Tuple example - tricky one: ', sliced_tuple)

print('##################################################################################')

# Handling Errors/Exception using try-except keywords: Python has a very useful statements, just designed for aim how to catch or handle run-time errors/exceptions, the same style in programming languages like Java or C#:

# Example 1 --> basic style:

try:
    # Try this print 1st one --> run the program
    print("Hello world!")
    # then comment below code-line it and run the program again
    print("Szia...", 1000/0) # division by zero --> will throw an exception called: ZeroDivisionError: raised when 2nd argument of a division or modulo operation is zero
except:
    print("Exception raised --> message to end-user: Something went wrong!") # message to display when exception/run-time error occured
else:
    print("Nothing went wrong") # else will handle message if exception/error cannot be handled
        
print("---------------------------------------------------------------------------------------------")
# Example 2 --> advanced style:

def my_divide(num1, num2):
    try:
        print(num1 / num2)
        # possible to code like this in catching multiple exceptions but....
        # except (TypeError, ZeroDivisionError):
    except TypeError as typeExceptionError: # define a variable to handle exception object itself --> that's exception instance
        print("RTE (Run-Time Error) --> Type Exception: encountered a problem!!")
        print(typeExceptionError)
        print("----------")
    except ZeroDivisionError as zeroExceptionError:
        print("RTE (Run-Time Error) --> Zero Division Exception: encountered a problem!!")
        print(zeroExceptionError)
        print("----------")

print('', my_divide(10,0))
print('', my_divide('Mohi',10))

print("---------------------------------------------------------------------------------------------")
# Example 3 --> How to use finally block style:
'''
Finally
    The finally block, if specified, will be executed regardless if the try
    block raises an error or not.
'''
try:
    print('No problem at all..')
except:
    print('Exception just happend! What!')
finally:
    print('finally block example: I will be always beside you..')
    
print('##################################################################################')

# Dictionary Python data structures or Map like in Java, an excellent data type to store items like in dictionary, synonym-dictionary, also search performance is really better that list Python data structure
#  Let us take a look how to use it and manipulate it's data (items/values):

# By definition --> Dictionary store indexes with keys that are mapped to specific values, they key-value pairs offer an excellent way of organizing/storing different data types easily:
#  key (or index) can be either a string, Boolean or integer data types:

# Simple dictionary example, later we can make it more complex (key: value)
employees_dict = {401: 'Sarah', 402: 'John', 403: 'Attila'}
empty_dict = {}
other_way_to_create_dict = dict() # using constructor of Object class dict
another_dict_example = {
        'car-brand': 'Kia',
        'car-type': 'Sportage',
        'car-model-year': 2018,
        'is-used-car': True,
        'car-price': 24.000,
        'price-currency': 'EUR'
    }

print('Simple Python dictionary example: ', employees_dict)
print('Empty Python dictionary example: ', empty_dict)
print('3rd way to create a Python dictionary example: ', type(other_way_to_create_dict))

# How to access any element within Python dictionary as below:
print('Access an element inside a Python dictionary example1: ', employees_dict[402])
print(f"Access an element inside a Python dictionary example2: car-brand name: {another_dict_example['car-brand']}, it's price in EUR: {another_dict_example['car-price']}00")

# Changing/updating an element-value within Python dictionary as below:
#  As example: let us change/update the car price to another amount:
another_dict_example['car-price'] = 33.000
print(f"Access an element inside a Python dictionary example2: car-brand name: {another_dict_example['car-brand']}, it's price in EUR: {another_dict_example['car-price']}00")

# Final thing how to iterate or loop keys, items/values within a specific given dictionary:
#  there are 3 types of loops trick exists for iterating or visiting each item in the dictionary, how?

# Example-Loop#1: loop/iterate all key/index names in the given dictionary:
for key_index in another_dict_example:
    print(f'another_dict_example [{key_index}] index-name')

print()

# Example-Loop#2: loop/iterate all values in the given dictionary:
for key_index in another_dict_example:
    print(f'another_dict_example [{key_index}] value = {another_dict_example[key_index]}')

print()

# Example-Loop#3: loop/iterate using key-value pairs in the given dictionary --> using dict.items() method, which will return a list of key-value tuple pairs
for key_index, item_value in another_dict_example.items():
    print(f'another_dict_example key-value pairs looping: {key_index, item_value}')
    
'''
Famous dictionary methods like:
#  dict.keys(): return a list of key names only
#  dict.values(): return a list of values only
'''

print('##################################################################################')

'''
Class definition and dealing with OOP (Object Oriented Programming) using Python language:

What is a Class definition in Python and any other language that support paradigm of OOP coding:
 Class are a blueprint or a set of instructions to build a specific type of object. It is a basic concept of Object-Oriented Programming which revolve around the real-life entities.
Class in Python determines how an object will behave and what the object will contain (source: https://www.guru99.com/java-oops-class-objects.html)

In other words:

If I would like to use: in programming/coding different attributes (data types: string, integer, dictionary, list, etc) and apply a different set of actions (i.e. methods) on it,
to reach specific behaviour, science say use OOP (Object Oriented Programming), by covering and defining all attributes and behaviours under one house called 'CLass' --> in IT
we say data-encapsulation.
'''
# Example: define the world of Platics using OOP style:
#  Plastic details original source from: https://en.wikipedia.org/wiki/Plastic#Common_plastics

# Main parent class
class PlasticClass:
    # All Python classes have a function called __init__(), which is always executed when the class is being initiated (default constructor).
    # Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created -- instance object creation:
    # 'self' keyword is obligatory in Python OOP coding style:
    def __init__(self, pType, pAbbrev, pUsed_in):
        print('PlasticClass:: __init__(): PlasticClass initializing the class object creation using default constructor style..')
        # Class fields or attributes (describe the paramters, what data to store inside your class)
        self.type = pType
        self.abbrev = pAbbrev
        self.used_in = pUsed_in
        self.quantity_to_manufacture = 0 # initial plastic manufactuing example: no orders!
        
    # Class methods: are functions that belongs to the object-instance (describe the behaviour)
    # 'self' keyword is obligatory in Python OOP coding style:
    def doManufactureSpecificQuantity(self, pQuantity):
        print('PlasticClass:: doManufactureSpecificQuantity(): inside the OOP class method/function..')
        self.quantity_to_manufacture = pQuantity

# use object instantiation to use your class in the coding part, without an object-instance creation you cannot do anything to reach your Class attributes or methods:
p1 = PlasticClass("Polyamides", "PA", ['fibers', 'toothbrush bristles', 'tubing', 'fishing line', 'low-strength machine parts: gun frame'])

print('Using 1st Example of Class object-instance creation....', type(p1))
print('Plastic-Type: ', p1.type)
print('Plastic-Abbreviation (Chemistry): ', p1.abbrev)
print('Plastic used-in for manufacturing: ', p1.used_in)
p1.doManufactureSpecificQuantity(10000)
print('Plastic total order (Quantity) to manufacture: ', p1.quantity_to_manufacture)

## You can also create as many object-instances for a class, as needed but BECAREFUL object-instance is really expensive for the memory and creating many with properly use them, will loose RAM.
##  that's why OOP applications are using a lot of RAM server and machines memory!

# use another object instantiation from your PlaticClass:
p2 = PlasticClass("Polyethylene", "PE", ['supermarket bags', 'plastic bottles'])

print('Using 2nd Example of Class object-instance creation....', type(p2))
print('Plastic-Type: ', p2.type)
print('Plastic-Abbreviation (Chemistry): ', p2.abbrev)
print('Plastic used-in for manufacturing: ', p2.used_in)
p2.doManufactureSpecificQuantity(100000000)
print('Plastic total order (Quantity) to manufacture: ', p2.quantity_to_manufacture)

# use another object instantiation from your PlaticClass:
p3 = PlasticClass("Polycarbonate + acrylonitrile butadiene styrene", "PC + ABS", ['mobile phone bodies', 'car interior and exterior parts'])

print('Using 3rd Example of Class object-instance creation....', type(p2))
print('Plastic-Type: ', p3.type)
print('Plastic-Abbreviation (Chemistry): ', p3.abbrev)
print('Plastic used-in for manufacturing: ', p3.used_in)
p3.doManufactureSpecificQuantity(10000000000)
print('Plastic total order (Quantity) to manufacture: ', p3.quantity_to_manufacture)

print('##################################################################################')

# Last topic I would like to highlight here: Recursion, means a function to call itself multiple time, until it meet the ending condition and by definition since beginning of programming in
#  1960s, a recursive function really important and have many benefits: https://techterms.com/definition/recursive_function:
#  A recursive function is a function that calls itself during its execution. The process may repeat several times, outputting the result and the end of each iteration
#  one of great benefits: code simplicity and efficiency using minimal amount of code, best function to describe recursive function is the math function:
#  Fibonacci sequence is the integer sequence of 0, 1, 1, 2, 3, 5, 8....The first two terms are 0 and 1. All other terms are obtained by adding the preceding two terms.
#  This means to say the nth term is the sum of (n-1)th and (n-2)th term, now how to write this in Python programming language:
#  Original code source: https://www.programiz.com/python-programming/examples/fibonacci-recursion

# Simple and elegant code:
def calcFibonacciSequenceRecursiveWay(n):
    if n <= 1:
        return n
    else:
        return (calcFibonacciSequenceRecursiveWay(n-1) + calcFibonacciSequenceRecursiveWay(n-2))
    
# Now use it and watch the generated int sequence number:
int_term = 15
print(f'Generate Fibonacci integer sequence of {int_term}')

# let us examine the generated int sequence (i.e. Fibonacci sequence) using a loop:
for index in range(0, int_term):
    print(f'Fibonacci[{index}]:= {calcFibonacciSequenceRecursiveWay(index)}')