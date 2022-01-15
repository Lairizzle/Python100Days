#=================================================
#Name: Paint Area Calculator Challenge
#Author: Keith Henderson - keith.donaldh@gmail.com
#Date: 2022-01-14
#=================================================

import math

#Create a calculator that will tell you how much paint you need.
def paintCalc(height, length, cover):
    numberOfCans = math.ceil((height*length)/cover)
    print(f"You will need {numberOfCans} cans of paint.")

wallH = int(input("Height of wall: "))
wallL = int(input("Length of wall: "))
coverage = 5
paintCalc(wallH, wallL, coverage)