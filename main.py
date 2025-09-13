'''We are going to write a program that generates a random number and asks the user to guess It.
If the player's guess is higher than the actual number , the program displays "Lower Number Please"
Similarly, if the user's guess is too low, the program prints :"higher number Please". when the user
guess the correct number than the program displays the number of guess the player used to arrive at the number.
 '''

import random
n=random.randint(1,100)
a=-1
guesses=0
while(a!=n):
    guesses+=1
    a=int(input("Guess the Number: "))
    if(a>n):
        print("Lower Number please")
    else:
        print("Higher Number please")

print(f"You have guess the number correctly in {guesses} attempt ")

