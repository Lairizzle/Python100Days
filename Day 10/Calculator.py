#=================================================
#Name: Calculator Project
#Author: Keith Henderson - keith.donaldh@gmail.com
#Date: 2022-01-16
#=================================================

#The first step will be creating functions for each operator

#Add
def add(n1, n2):
    return n1 + n2

#Subtract
def sub(n1, n2):
    return n1 - n2

#Multiply
def multiply(n1, n2):
    return n1 * n2

#Divide
def divide(n1, n2):
    return n1 / n2

#Dict of functions
operations = {
    "+": add, 
    "-": sub, 
    "*": multiply, 
    "/": divide
    }

def calculator():
    #Take user input
    num1 = float(input("What is the first number?: "))
    print("Please choose from the following operators: ")
    for i in operations:
        print(i)
    shouldContinue = True

    while shouldContinue:
        operatorChoice = input("Which operator would you like to use?: ")
        num2 = float(input("What is the next number?: "))

        #Pass input to get proper function to use from dict
        function = operations[operatorChoice]
        resultOne = function(num1, num2)

        print(f"The formula {num1} {operatorChoice} {num2} answer is {resultOne}")
        exitChoice = input("Would you like to continue to calculate with previous result?: Y/N ").lower()

        if exitChoice == "n":
            shouldContinue = False
            calculator()
        else:
            num1 = resultOne

calculator()