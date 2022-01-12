#=================================================
#Name: Reeborg Answer
#Author: Keith Henderson - keith.donaldh@gmail.com
#Date: 2022-01-11
#=================================================

def turnAround():
    turn_left()
    turn_left()
    turn_left()
    move()

for i in range(0, 6):
    move()
    turn_left()
    move()
    turnAround()
    turnAround()
    turn_left()