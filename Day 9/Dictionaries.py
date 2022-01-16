#=================================================
#Name: Dictionaries
#Author: Keith Henderson - keith.donaldh@gmail.com
#Date: 2022-01-15
#=================================================

#Dictionaries allow you to group and tag related information
#Every dict has a key and a value - similar to a data table
#{Key: Value}
#Keys can be strings or integers

programmingDict = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again."
}

print(programmingDict["Bug"])

#Adding new items to a dict
programmingDict["Loop"] = "The action of doing something repeatedly."
print(programmingDict)

#Creating and empty dict
emptyDict = {}

#Edit item in existing dict
programmingDict["Bug"] = "An error in a program"
print(programmingDict)

#Loop through a dict
for item in programmingDict:
    print(item)
    #Get the value
    print(programmingDict[item])

#Clear existing dict
programmingDict = {}
print(programmingDict)

