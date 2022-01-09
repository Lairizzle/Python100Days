#=================================================
#Name: Nested If Statements
#Author: Keith Henderson - keith.donaldh@gmail.com
#Date: 2022-01-08
#=================================================

#Using the roller coaster example, once height is evaluated we evaluate
#the age to see the ticket price.

print("Welcome to the roller coaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride, you are tall enough!")
    age = int(input("What is your age?: "))
    
    if age < 12:
        print("You are less than 12 and must pay $5 dollars for a ticket.")
    elif age <= 18:
        print("You are between 12 and 18 and must pay $7 for a ticket.")
    else:
        print("You are over 18 and must pay $12 for a ticket.")
else:
    print("Sorry, you are not tall enough to ride!")