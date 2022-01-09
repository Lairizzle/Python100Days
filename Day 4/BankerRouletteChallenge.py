#=================================================
#Name: Banker Roulette Code Challenge
#Author: Keith Henderson - keith.donaldh@gmail.com
#Date: 2022-01-09
#=================================================
import random

print("Welcome to banker dinner roulette!")
dinnerGuests = input("Provide the dinner guests names seperated by a comma and a space: ")

names = dinnerGuests.split(", ")

x = random.randint(0, len(names)-1)

print(f"Congratulations! {names[x]} will be paying the bill!")

