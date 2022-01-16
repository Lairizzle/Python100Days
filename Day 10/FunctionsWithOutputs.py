#=================================================
#Name: Functions with Outputs   
#Author: Keith Henderson - keith.donaldh@gmail.com
#Date: 2022-01-16
#=================================================

#Functions can take an input and also provide an output

def myFunction():
    result = 3 * 2
    #to return an output you use the return keyword
    return result

output = myFunction()
print(output)


def formatName(fName, lName):
    fName = fName.title()
    lName = lName.title()
    return (fName + " " + lName)


print(formatName("keith", "henderson"))

