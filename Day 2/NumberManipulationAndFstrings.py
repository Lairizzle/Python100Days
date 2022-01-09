#=================================================
#Name: Number Manipulation and F Strings
#Author: Keith Henderson - keith.donaldh@gmail.com
#Date: 2022-01-07
#=================================================

#Rounding round(<calculation>, <number of decimals>)
print(round(8/3, 2))
print(round(8/3, 3))
print(round(8/3, 4))

#Floor Division // (rounds down to nearest whole number)
print(8 // 3)

#Using operators to add to existing variables
#Long form
num = 1
num  = num + 1
print(num)

#Shorthand operators
# +=, -=, *=, /=

#Addition
num += 1
print(num)

#Subtraction
num -= 1
print(num)

#Multiplication
num *= 1
print(num)

#Division
num /= 1
print(num)

#To print a combination of data types in outputs you can use f strings.
score = 10
height = 1.8
isWinning = True

print(f"Your score is {score}, your height is {height} and you are winning is {isWinning}.")

