#=================================================
#Name: Rock, Paper, Scissors Game
#Author: Keith Henderson - keith.donaldh@gmail.com
#Date: 2022-01-09
#=================================================

import random

print("Welcome to Rock, Paper Scissors!")
playerSelection = int(input("Enter your choice to battle the computer, Type 0 for Rock, 1 for Paper or 2 for Scissors: "))

playerHand = ["rock","paper","scissors"]
computerHand = ["rock","paper","scissors"]

computerSelection = random.randint(0,2)

playerResult = playerHand[playerSelection]
computerResult = computerHand[computerSelection]

if playerSelection == computerSelection:
    winOrLose = "It is a draw!"
elif playerSelection == 2 and computerSelection == 1 :
    winOrLose = "You win!"
elif playerSelection == 1 and computerSelection == 0 :
    winOrLose = "You win!"
elif playerSelection == 0 and computerSelection == 2:
    winOrLose = "You win!"
else:
    winOrLose = "You lose!"

print(f"You chose {playerResult} and the computer chose {computerResult}!")
print(f"{winOrLose}!")



