#=================================================
#Name: Index Errors and Nested Lists
#Author: Keith Henderson - keith.donaldh@gmail.com
#Date: 2022-01-09
#=================================================

canadianProvinces = ["Ontario","Alberta","British Columbia", "Manitoba", "New Brunswick"
"Nova Scotia", "Prince Edward Island", "Quebec", "Saskatchewan", "Yukon", "Newfoundland",
"Nunavut"]

#Since list indexes start at 0, if you reference something outside the number of index items you will get an error
lengthOfList = len(canadianProvinces)

#The list above has 11 items. If you were to reference index 11 it would throw an error
#The len() function provides the total number, we need to offset this index by 1 to avoid the error
print(lengthOfList)
print(canadianProvinces[lengthOfList-1])

#Nested Lists
fruits = ["Strawberry","Apples","Grapes","Peaches"]
vegtables = ["Spinach","Kale","Tomatoes","Celery"]

nestedList = [fruits, vegtables]
print(nestedList)
