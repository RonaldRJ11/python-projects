import random
from words import word
from logo import logo_symbol
from logo import stages

print(f"Welcome to\n{logo_symbol}")

def game(life):
    a = input("Guess a letter: ")
    if a in choose:
        print("Right Guess!!!")
        for letter in range(len(choose)):
            if a == choose[letter]:
                blank[letter] = choose[letter]
        print("".join(blank))
        return life
            
    else:
        print("Wrong Guess!!!")
        life -= 1
        print(stages[life])
        return life

choose = random.choice(word)
blank = ["_" for i in range(len(choose))]
print("".join(blank), "===== Guess the", len(blank), "letter word")
life = 6

while life >= 1 and "_" in blank:
    life = game(life)
    print(f"Life balance = {life}")

if "_" not in blank:
    print("***** CONGRADULATIONS, YOU WON THE GAME *****")

else:
    print("***** SORRY, BETTER LUCK NEXT TIME *****\nThe Hangman word is", choose)

