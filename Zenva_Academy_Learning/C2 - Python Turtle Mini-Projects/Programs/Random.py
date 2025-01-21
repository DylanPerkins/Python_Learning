from random import *
from turtle import *

# Will generate random number between x and xx, here it's 1 and 10
random_number = randrange(1, 10)
print(random_number)

forward(randrange(20, 200))
right(randrange(0, 360))
forward(randrange(20, 200))

done()