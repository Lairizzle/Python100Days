#=================================================
#Name: Caesar Cipher
#Author: Keith Henderson - keith.donaldh@gmail.com
#Date: 2022-01-14
#=================================================

#Creating a caesar cipher
#Insert text and shift by desired amount

alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 
'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
'u', 'v', 'w', 'x', 'y', 'z']

shouldContinue = True
while shouldContinue:
    direction = input("Type 'encode' to encrypt a message, or 'decode' to decrypt: ")
    text = input("Type your message: ").lower()
    shift = int(input("Type the shift number: "))
    shift = (shift % 26) - len(alpha)

    def caesar(text, shift, direction):
        encryption = ""
        if direction == "decode":
            shift *= -1
            shift -= len(alpha)
        for letter in text:
            if letter in alpha:
                pos = alpha.index(letter)
                encryption += alpha[pos+shift]
            else:
                encryption += letter
        print(f"Your {direction}d text is: {encryption}")

    caesar(text, shift, direction)

    result = input("Do you want to continue? Y/N: ").lower()
    if result == "n":
        shouldContinue = False


