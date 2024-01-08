from turtle import *

#Conditions allow us to check if a statement is true or false and execute code based on that outcome.

#creating variables
a=5
b=5
c=4
d=24
e=35
f=2

#will print out statement if true
if a==b:
    print("a is equal to b")



if c<d:
    print("c is less than d")

if e>f:
    print("e is greater than f")

######################
#   Else statements
######################

# Consider the algorithm below where different messages print out based on whether or not your name is "Jack"

#name variable
name = "Annika"

#prints statement if your name is Jack
if name == "Jack":
    print("You are Jack")

#prints statement if your name is not Jack
if name != "Jack":
    print("You are not Jack")

#A better way to write algorithm is with an else statement which executes the following code if the if statement is false 
name = "Jack"
if name == "Jack":
    print("You are Jack")

else:
    print("You are not Jack")

######################
#   Elseif statements
######################

#These statements are a combination of else if statements. Consider the following algorithm. 

name = "Bob"
if name == "Jack":
    print("You are Jack")

elif name == "Bob":
    print("You are Bob")

else:
    print("You are not Jack or Bob")

#   The algorithm follows the pattern of If this is true, do this. Otherwise, if this is true, do this. 
#   If none of those things were true, then do this. So, in this examples; 

#   If the name is Jack, print "You are Jack"
#   However, if the name is Bob print "You are Bob"
#   If the name is neither Jack nor Bob, print "You are not Jack or Bob"
print(54*0.25)