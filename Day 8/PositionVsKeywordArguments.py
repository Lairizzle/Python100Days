#=================================================
#Name: Positional Vs Keyword Arguments
#Author: Keith Henderson - keith.donaldh@gmail.com
#Date: 2022-01-14
#=================================================

#Positional Arguments
# def myFunction(1,2,3):
def greetWith(name, location):
    print(f"Hello {name}.")
    print(f"What is it like in {location}?")

greetWith("Keith", "Canada")

#Keyword Arguments
# def myFunction(a,b,c)
# myFunction (a=1, b=2, c=3)

greetWith(name="Keith", location="Canada")

