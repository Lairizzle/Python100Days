#=================================================
#Name: BMI Calculator 2.0
#Author: Keith Henderson - keith.donaldh@gmail.com
#Date: 2022-01-07
#=================================================

height = input("Enter your height in meters: ")
weight = input ("Enter your weight in kg: ")

result = int(int(weight) / float(height) ** 2)

if result < 18.5:
    print(f"Your BMI is {result}, you are underweight.")
elif result < 25:
    print(f"Your BMI is {result}, you are normal weight")
elif result < 30:
    print(f"Your BMI is {result}, you are overweight")
elif result < 35:
    print(f"Your BMI is {result}, you are obese")
else:
    print(f"Your BMI is {result}, you are clinically obese")