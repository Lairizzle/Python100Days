#=================================================
#Name: Password Generator Project
#Author: Keith Henderson - keith.donaldh@gmail.com
#Date: 2022-01-10
#================================================

#This will generate a password based on requested user input

import random

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
"A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
numbers = ["1","2","3","4","5","6","7","8","9","0"]
symbols = ["!","@","#","$","%","^","&","*","+"]

combinedCharacters = []

print("Welcome to the password generator!")

letterCount = int(input("How many letters would you like in your password?: "))
numberCount = int(input("How many numbers would you like in your password?: "))
symbolCount = int(input("How many symbols would you like in your password?: "))

for x in range(1, letterCount+1):
    maxLength = len(letters)
    #Originally solved the way below, same result but not as clean as random.choice()
    #combinedCharacters.append(letters[random.randint(0, maxLength-1)])
    combinedCharacters.append(random.choice(letters))

for y in range(1, numberCount+1):
    maxLength = len(numbers)
    #Originally solved the way below, same result but not as clean as random.choice()
    #combinedCharacters.append(numbers[random.randint(0, maxLength-1)])
    combinedCharacters.append(random.choice(numbers))

for z in range(1, symbolCount+1):
    maxLength = len(symbols)
    #Originally solved the way below, same result but not as clean as random.choice()
    #combinedCharacters.append(symbols[random.randint(0, maxLength-1)])
    combinedCharacters.append(random.choice(symbols))

random.shuffle(combinedCharacters)

outPutString = ""

for i in combinedCharacters:
    outPutString += i

print(f"Your password is: {outPutString}")
