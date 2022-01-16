#=================================================
#Name: Functions with Multiple Outputs
#Author: Keith Henderson - keith.donaldh@gmail.com
#Date: 2022-01-16
#=================================================

#Creating a function with multiple outputs
#Return can act as an escape as it always exists the function

def formatName(fName, lName):
    if fName == "" or lName == "":
        return "Invalid input."
    fName = fName.title()
    lName = lName.title()
    return (fName + " " + lName)

print(formatName(input("What is your first name? "), input("What is your last name? ")))
