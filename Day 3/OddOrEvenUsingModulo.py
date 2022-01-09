#=================================================
#Name: Odd or Even Code Challenge
#Author: Keith Henderson - keith.donaldh@gmail.com
#Date: 2022-01-08
#=================================================

#Use if, else and modulo to determine if the number is even or odd.
number = int(input("Which number do you want to check?: "))

result = number % 2

if result > 0:
    print("This number is odd.")
else:
    print("This number is even.")