#BMI Calculator Challenge
height = input("Enter your height in meters: ")
weight = input ("Enter your weight in kg: ")

result = int(weight) / float(height) ** 2

print(int(result))