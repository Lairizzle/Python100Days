#=================================================
#Name: FizzBuzz Job Interview Question
#Author: Keith Henderson - keith.donaldh@gmail.com
#Date: 2022-01-10
#=================================================

#Fizz Buzz Rules:
#Count from 1 to 100
#If the number is divisible by 3 then it should print Fizz
#If the number is divisible by 5 then it should print Buzz
#If it divisible by both 3 and 5 it should print FizzBuzz

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)