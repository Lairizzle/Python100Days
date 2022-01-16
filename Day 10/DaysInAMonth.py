#=================================================
#Name: Days in Month Coding Challenge
#Author: Keith Henderson - keith.donaldh@gmail.com
#Date: 2022-01-16
#=================================================

#This challenge is to create a function which will take year and month
#Then it will use this information to work out the number of days in the month
#It will then return the output

def daysInAMonth(year, month):
    monthDays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                leapBool = True
            else:
                leapBool = False
        else:
            leapBool = True
    else:
        leapBool = False

    if leapBool == True and month == 2:
        return monthDays[month-1]+1
    else:
        return monthDays[month-1]



year = int(input("Please provide a year: "))
month = int(input("Please provide a month: "))
days = daysInAMonth(year, month)
print(f"In the year {year}, the {month} month had {days} days.")

