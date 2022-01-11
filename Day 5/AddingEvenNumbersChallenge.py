#=================================================
#Name: Adding Even Numbers Challenge
#Author: Keith Henderson - keith.donaldh@gmail.com
#Date: 2022-01-10
#=================================================

#This challenge requires to print total amount of even numbers from 1 to 100

total = 0
for i in range(0, 101, 2):
    total += i
print(f"The total number of even numbers from 1 to 100 is {total}.")