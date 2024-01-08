#   you want to code printing numbers 1-10 on increments of one. You could write num=0 then num=num+1 all the way up to 10,
#   but that quickly becomes tedious. For loops allow you to complete repetitive processes without having to manually jot down
#   the commands. 

#   For this, we write the for keyword, the name of a temporary variable, then the in keyword, and a range to define the number  
#   of times we want to iterate upon this loop. Lastly, we enter the colon symbol and go to a new line to start the indented 
#   block of code for our for loop. Consider the for loop below that prints the numbers 1-10
#creating variable
num = 0

#for a value x in range 10. The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1  
for x in range(10):
    num = num + 2
    print(num)

from turtle import *

#function that moves forward 50 pixels and turns right at a given angle
def move_and_turn(angle):
    forward(50)
    right(angle)

# draw a square 
for x in range(4):
    move_and_turn(90)

#move forward 50 pixels no line 
penup()
forward(50)
pendown()

#draw a hexagon 
for x in range(6):
    move_and_turn(60)

#move forward 50 pixels no line 
penup()
forward(50)
pendown()

#Write the code for an octagon above with a for loop using the function below.
for x in range(8):
    move_and_turn(45)

#move forward 50 pixels no line 
penup()
forward(50)
pendown()

#draw a decagon
for x in range(10):
    move_and_turn(36)

penup()
forward(50)
pendown()

#draw a dodecagon
for x in range(12):
    move_and_turn(30)

# A for loop iterates for a set number of times. There’s also another type of loop, 
# known as a while loop. A while loop will iterate upon the block of code as long 
# as a given condition is true. Here are examples of a while loop that prints number 1-10

x=0
while x < 11:
    print(x)
    x += 1

# let's say you only want to run a loop a certain amount of times a break function will 
# allow you to do that. An example is show below 

for x in range(100):
    print(x)
    if x == 50:
        break