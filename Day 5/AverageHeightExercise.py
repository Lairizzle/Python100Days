#=================================================
#Name: Average Height Exercise
#Author: Keith Henderson - keith.donaldh@gmail.com
#Date: 2022-01-10
#=================================================

#In this challenge we enter a list of heights
#Then we use the for loop to figure our the average height


studentHeights = input("Enter a list of student heights: ").split()
for i in range(0, len(studentHeights)):
    studentHeights[i] = int(studentHeights[i])
print(studentHeights)

total = 0
count = 0

for height in studentHeights:
    total += height
    count += 1
    
averageHeight = round(total/count)
print(f"The average height is {averageHeight}.")