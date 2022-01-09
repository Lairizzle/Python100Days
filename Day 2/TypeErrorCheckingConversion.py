#=================================================
#Name: Type Error Checking and Conversions
#Author: Keith Henderson - keith.donaldh@gmail.com
#Date: 2022-01-07
#=================================================

#Example variables
name = "Keith"
number = 8

#Type Checking example, you can check variables to see what kind of data type you are working with
print(type(name))
print(type(number))

#Type conversion
newNumber = str(number)
print(type(newNumber))

newNumber = float(number)
print(type(newNumber))

#Coding Challenge
#Take a two digit number through input and calculate it
userInput = input("Enter a two digit number: ")
#Check the type of input
print(type(userInput))
#Print the input and subscript the input, then convert to integer and add together.
print(int(userInput[0]) + int(userInput[1]))



