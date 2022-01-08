#Weeks in your life challenge
age = input("What is your age?: ")

#Calculate days, weeks and months left.
age = int(age)
days = (90-age) * 365
weeks = (90-age) * 52
months = (90-age) * 12

#print results
print(f"You have {days} days left, {weeks} weeks left and {months} months left.")