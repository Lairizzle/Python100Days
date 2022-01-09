#=================================================
#Name: BMI Calculator Challenge
#Author: Keith Henderson - keith.donaldh@gmail.com
#Date: 2022-01-07
#=================================================

height = input("Enter your height in meters: ")
weight = input ("Enter your weight in kg: ")

result = int(weight) / float(height) ** 2

print(int(result))