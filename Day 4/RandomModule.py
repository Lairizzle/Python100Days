#=================================================
#Name: Random Module
#Author: Keith Henderson - keith.donaldh@gmail.com
#Date: 2022-01-09
#=================================================
#Creating randomness in a program

import random
import myModule #importing a custom module existing in working directory

#Random int
x = random.randint(1, 10)
print(x)

#Random float
y = random.random()
z = 5
print(y*5)

print(myModule.name)