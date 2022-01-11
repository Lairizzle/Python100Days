#=================================================
#Name: Highest Score Challenge
#Author: Keith Henderson - keith.donaldh@gmail.com
#Date: 2022-01-10
#=================================================

#This is the highest score challenge
#This will take in a list of scores and determine the highest value
#Do not use min or max functions.

studentScores = input("Input a list of student scores: ").split()
for x in range(0, len(studentScores)):
    studentScores[x] =int(studentScores[x])
print(studentScores)

highScore = 0

for score in studentScores:
    if score > highScore:
        highScore = score

print(f"The highest student score is {highScore}.")

