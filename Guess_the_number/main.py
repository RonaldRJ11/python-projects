import random
import os
from logo import game_logo

def guess_number():
    global chance
    if chance > 0:
        temp = int(input("Guess the number between 1 and 100 : "))
        if temp > num:
            chance -= 1
            print(f"Too high.\nRemaining guesses : {chance}\nGuess Again...")
            guess_number()
        elif temp < num:
            chance -= 1
            print(f"Too low.\nRemaining guesses : {chance}\nGuess again...")
            guess_number()
        else:
            print(f"You got it, the answer is {num}")
            start_game()
    else:
        print(f"You've ran out of guessess, the answer is {num}")
        start_game()

def start_game():
    global num
    global chance
    if input("Do you want to start the game? (y/n) : ") == "y":
        os.system("cls")
        print(game_logo)
        if input("Choose the difficulty - (easy or hard) : ") == "hard":
            chance = 5
        else:
            chance = 10
        num = random.randint(1,100)
        guess_number()
    else:
        print("*****Thankyou*****")

num = chance = 0
start_game()