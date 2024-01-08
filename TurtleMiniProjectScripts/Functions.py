from turtle import *

# Consider the following code

print("Hello Bob")


# if you wanted to change something to structure (e.g. add exclamation point) 
# it would have to be added to each line which is tedious and impractical at
# a large scale. This process can be simplified with functions. Consider the 
#following function:

def say_hello(name):
    print("Hello " + name)

#To define a function we type the def keyword, then the name of the function, 
# and we can pass in the parameters or arguments for this function in between 
# parentheses (e.g. name): (the colon is very important)

#Inside our function, we want to call the print function passing in the 
# concatenation of “Hello” and the name sent as parameter.

# To call it, go to a new line and write down the name of the function 
# alongside the parameter you want to send over: Examples of calling the 
# function are shown below

say_hello("Steve")

#Now, if we need to alter the phrase being printed, we do it only once directly 
# where we’re defining our function as shown below

def say_hello(name):
    print("How are you " + name)

say_hello("Mary")

# Here is an example of a function that moves a certain distance, turns right a
# certain angle, then moves forward the same distance again

speed(1)

def move_and_turn(distance, angle):
    forward(distance)
    right(angle)
    forward(distance)

move_and_turn(100, 90)

#return command allows the use of variables outside of a function. Without return, 
# variables created inside a function only exist in the function. The variable name 
# only exists in the function, however you can retrieve the value of a variable. See
# below for an example. 

def add_numbers (a, b):
    sum = a + b
    return sum
num = add_numbers(150, 2063)

done()