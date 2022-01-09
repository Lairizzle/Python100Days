#=================================================
#Name: Love Calculator Challenge
#Author: Keith Henderson - keith.donaldh@gmail.com
#Date: 2022-01-07
#=================================================

print("Welcome to the love calculator!")
nameOne = input("What is your name?: ")
nameTwo = input("What is your crush's name?: ")

nameOne = nameOne.lower()
nameTwo = nameTwo.lower()
combinedNames = nameOne+nameTwo

trueCount = (combinedNames.count("t")
+combinedNames.count("r")
+combinedNames.count("u")
+combinedNames.count("e"))

loveCount =(combinedNames.count("l")
+combinedNames.count("o")
+combinedNames.count("v")
+combinedNames.count("e"))

loveScore = int(str(trueCount)+str(loveCount))

if loveScore < 10 or loveScore > 90:
    print(f"Your love score is {loveScore}%, you go together like coke and mentos.")
elif loveScore >= 40 or loveScore <= 50:
    print(f"Your love score is {loveScore}%, you are alright together.")
else:
    print(f"Your love score is {loveScore}%.")
