#=================================================
#Name: Docstrings
#Author: Keith Henderson - keith.donaldh@gmail.com
#Date: 2022-01-16
#=================================================

#Doc strings allow us to make commentary as we are coding.
#This lets you explain what a function does 

def formatName(fName, lName):
    """Take a first and last name and format it and return a title case."""
    fName = fName.title()
    lName = lName.title()
    return (fName + " " + lName)


print(formatName("keith", "henderson"))
