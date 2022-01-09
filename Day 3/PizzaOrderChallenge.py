#=================================================
#Name: Pizza Order Challenge
#Author: Keith Henderson - keith.donaldh@gmail.com
#Date: 2022-01-08
#=================================================

print("Welcome to the Pizza Py Delivery Program!")

size = input("What size pizza would you like? S, M or L?: ")
addPepperoni = input("Would you like to add pepperoni? Y or N: ")
extraCheese = input("Would you like to add extra cheese?: Y or N: ")
totalBill = 0

if size == "S":
    totalBill += 15
elif size == "M":
    totalBill += 20
elif size == "L":
    totalBill += 25
else:
    totalBill += 25
    print("You entered something weird so we charged you for a large.")

if addPepperoni == "Y":
    if size == "S":
        totalBill += 2
    else:
        totalBill += 3

if extraCheese == "Y":
    totalBill += 1

print(f"Your total bill for the pizza py is ${totalBill}.") 