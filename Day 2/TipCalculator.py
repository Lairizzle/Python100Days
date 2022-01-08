#Tip Calculator Project
print("Welcome to the tip calculator")
totalBill = input("What was the total bill?: ")
percentageTip = input("What percentage tip would you like to give? 10, 12, or 15?: ")
numberToSplit = input("How many people to slip the bill?: ")


result = (float(totalBill)*(1+float(percentageTip)/100))/float(numberToSplit)
result = round(result,2)
print(f"Each person should pay ${result}")