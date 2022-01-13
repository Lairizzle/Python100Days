#=================================================
#Name: Hangman Game
#Author: Keith Henderson - keith.donaldh@gmail.com
#Date: 2022-01-12
#=================================================

import random
from replit import clear

print("Welcome to Hangman!")

#Step One
#Choosing a random word from a list
wordList = ["ardvark", "baboon", "camel"]
randomWord = random.choice(wordList)
answerList = []

for letter in randomWord:
    answerList +=  "_"

breakLoop = False
playerLives = 6

while not breakLoop:

    #Grab user input
    userInput = input("Guess a letter in the word: ").lower()
    clear()

    if userInput in answerList:
        print(f"You already guessed the letter {userInput}, try another!")

    #Loop through and check which letters exist in random word based on user input
    for index in range(0, len(randomWord)):
        letter = randomWord[index]
        if userInput == letter:
            answerList[index] = letter
    print(answerList)

    if userInput in randomWord:
        print(f"Correct. The letter {userInput} is in the word!")

    if userInput not in randomWord:
        playerLives -= 1
        print(f"Incorrect. You lose a life. You now have {playerLives} lives remaining.")

    if playerLives == 0:
        breakLoop = True
        print("You Lost!")

    if "_" not in answerList:
        breakLoop = True
        print("You won!!")



