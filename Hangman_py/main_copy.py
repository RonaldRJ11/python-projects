import random
import os
from words import word
from logo import logo_symbol
from logo import stages
os.system("cls")
print(f"Welcome to\n{logo_symbol}")

def game_start(choose, blank, life):
    temp = input("Press enter to start!!!")
    os.system("cls")
    choose = random.choice(word)
    blank = ["_" for i in choose]
    life = 6
    print(stages[life])
    print(" ".join(blank), f"===== Guess the {len(blank)} letter word\n\n")


    while life >= 1 and "_" in blank:
        life = game(life, choose, blank)
        print(f"life balance = {life}\n\n")
    rep_process(rep, blank, choose)


def game(life, choose, blank):
    a = input("Guess a letter: ")
    if a in choose:
        for letter in range(len(choose)):
            if a == choose[letter]:
                blank[letter] = choose[letter]
        os.system("cls")
        print(f"{stages[life]}\n{a} is an Right Guess!!!\n{' '.join(blank)}\n\n")
        return life
    
    else:
        life -= 1
        os.system("cls")
        print(f"{stages[life]}\n{a} is an Wrong Guess!!!\n{' '.join(blank)}\n\n")
        return life


def rep_process(rep, blank, choose):
    if "_" not in blank:
        print("***** CONGRADULATIONS, YOU WON THE GAME *****\n\n")

    else:
        print(f"***** SORRY, BETTER LUCK NEXT TIME *****\n\nThe Hangman word is {choose}\n\n")
    
    rep = input("Do you want to play again!!! Type 'yes' or 'no'\n")
    if rep == "yes":
        game_start(choose, blank, life)
    else:
        print("Thankyou, Nice Play!!!")

choose = ""
blank = []
life = 0
rep = ""
game_start(choose, blank, life)