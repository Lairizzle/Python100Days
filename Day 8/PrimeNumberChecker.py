#=================================================
#Name: Prime Number Checker
#Author: Keith Henderson - keith.donaldh@gmail.com
#Date: 2022-01-14
#=================================================


def primeCheck(n):
    totalDivisible = 0
    for i in range(1, n+1):
        if n % i == 0:
            totalDivisible += 1
    if totalDivisible > 2:
        print(f"{n} is not a prime number.")
    else:
        print(f"{n} is a prime number.")



number = int(input("Check this number for prime: "))
primeCheck(number)