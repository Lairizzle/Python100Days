#=================================================
#Name: Multiple If Statements
#Author: Keith Henderson - keith.donaldh@gmail.com
#Date: 2022-01-08
#=================================================

print("Welcome to the roller coaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride, you are tall enough!")
    age = int(input("What is your age?: "))
    
    if age < 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    else:
        bill = 12
        print("Adult tickets are $12.")

    wantsPhoto = input("Do you want a photo taken? Y or N: ")

    if wantsPhoto == "Y":
        bill += 3
        print(f"With the photo your total ticket will cost ${bill}.")
    else:
        print(f"Without the photo your total ticket will cost ${bill}.")
else:
    print("Sorry, you are not tall enough to ride!")