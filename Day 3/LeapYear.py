#=================================================
#Name: Leap Year Code Challenge
#Author: Keith Henderson - keith.donaldh@gmail.com
#Date: 2022-01-08
#=================================================

year = int(input("Which year do you want to check?: "))

print(year % 4)
print(year % 100)
print(year % 400)

if (year % 4) == 0:
    if (year % 100) == 0:
        if (year % 400) == 0:
            print(f"{year} is a leap year.")
        else:
            print(f"{year} is not a leap year.")
    else:
        print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
