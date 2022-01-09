#=================================================
#Name: Treasure Map Code Challenge
#Author: Keith Henderson - keith.donaldh@gmail.com
#Date: 2022-01-09
#=================================================

#This challenge is to mark a spot with X

row1 = [" "," "," "]
row2 = [" "," "," "]
row3 = [" "," "," "]

map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
x = input("Where do you want to place your treasure? Use two digits both between 1-3: ")

#Long form
h = int(x[0])
v = int(x[1])

selectedRow = map[v-1]
selectedRow[h-1] = "X"
print(f"{row1}\n{row2}\n{row3}\n")

#Short Form
#map[int(x[0])-1][int(x[1])-1] = "X"
#print(f"{row1}\n{row2}\n{row3}")