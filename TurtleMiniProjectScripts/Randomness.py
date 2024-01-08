#importing random  and turtle library 
from random import *
from turtle import *

#generate random number 1-10
random_number = randrange(1, 10)
print(random_number)

#move forward between 20-100 pixels
forward(randrange(20, 100))

#turn right between 0-360 degrees
right(randrange(0, 360))

#move forward between 20-100 pixels
forward(randrange(20, 100))

#prevent graphics window from closing 
done()