#=================================================
#Name: Treasure Island Choose Your Own Adventure
#Author: Keith Henderson - keith.donaldh@gmail.com
#Date: 2022-01-07
#=================================================

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
direction = input("You're at a crossroad, where do you want to go? left or right?: ").lower()

if direction == "left":
    swimOrwait = input("You are are standing at a river. Do you wait for the boat or try to cross?: ").lower()
    
    if swimOrwait == "wait":
        doorChoice = input("You find yourself before 3 doors. Red, Yellow and Blue... which do you choose?: ").lower()

        if doorChoice == "yellow":
            print("You stumble through the door and discover treasure. You are a billionaire and invest everything you find into blockchain.")
        elif doorChoice == "red":
            print("You open the door and are consumed by flames and die a fiery death. Game Over.")
        elif doorChoice == "blue":
            print("You open the door and are eaten by a dragon. Game Over.")
        else:
            print("You didn't pick a door, instead you stood in one spot and died of starvation. Game Over.")
    else: 
        print("You tried to cross and ended being attacked by trout and drowning. Game Over")
else:
    print("You turned right and fell into a hidden pit. Game Over.")