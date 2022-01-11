#=================================================
#Name: For Loops and The Range Function
#Author: Keith Henderson - keith.donaldh@gmail.com
#Date: 2022-01-10
#=================================================

#You can use the range function to loop a specific number of times
#The range function looks like range(a, b)

#Range will only print to the second range argument -1 (e.g 9)
for i in range(1,10):
    print(i)

#You can step through a range by adding a third argument
for i in range(1, 10, 3):
    print(i)

#Gauss example
total = 0
for i in range(1,101):
    total += i
print(total)