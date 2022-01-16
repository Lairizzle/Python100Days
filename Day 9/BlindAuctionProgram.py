#=================================================
#Name: Blind Auction Program
#Author: Keith Henderson - keith.donaldh@gmail.com
#Date: 2022-01-15
#=================================================

#Loop through three times to let three people place a bid

bidders = {}
print("Welcome to the silent auction!")

def bidProgram():
    shouldContinue = True
    while shouldContinue:
        userName = input("What is your name?: ")
        bid = int(input("What is your bid?: "))
        bidders[userName] = bid
        continueBid = input("Is there another bidder? Y/N: ").lower()

        if continueBid == "n":
            shouldContinue = False

    highestBid = 0
    for bidder in bidders:
        if bidders[bidder] > highestBid:
            highestBidder = bidder
            highestBid = bidders[bidder]
    print(f"The highest bidder is: {highestBidder} with a bid of ${highestBid}!")

bidProgram()






