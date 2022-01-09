#=================================================
#Name: Lists
#Author: Keith Henderson - keith.donaldh@gmail.com
#Date: 2022-01-09
#=================================================

#Lists are data structure and a way to store and organize data
#Lists and arrays start at 0, not 1. The index is based on the offset. The first item has no offset or 0.

canadianProvinces = ["Ontario","Alberta","British Columbia", "Manitoba", "New Brunswick"
"Nova Scotia", "Prince Edward Island", "Quebec", "Saskatchewan", "Yukon", "Newfoundland",
"Nunavut"]

#First item using 0
print(canadianProvinces[0])

#Last item using a negative index
print(canadianProvinces[-1])

#You can change items in a list
canadianProvinces[0] = "Untario"
print(canadianProvinces)

#Adding items to the end of a list
canadianProvinces.append("Keithland")
print(canadianProvinces)

#Extend function
canadianProvinces.extend(["Kyleland","Randomland"])
print(canadianProvinces)

#check documentation for other list functionality