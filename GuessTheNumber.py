# Day 12 - Jun 30 '24
# Guess The Number Game

import random

logo = r'''
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ' _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|        
'''

def play_game():
    print(logo)
    print("Welcome to the Number Guessing Game!\n")
    print("I'm thinking of a number between 1 and 100.\n")

    number = random.randint(1, 100)

    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

    if difficulty == 'easy':
        lives = 10
    else:
        lives = 5

    while lives > 0:
        print(f"You have {lives} attempts remaining to guess the number.")
        guess = input("Make a guess: ")
        
        if not guess.isdigit():
            print("Invalid input. Please enter a number.")
            continue
        
        guess = int(guess)

        if guess > number:
            print("Too High. \n Guess again.")
            lives -= 1
        elif guess < number:
            print("Too Low. \n Guess again.")
            lives -= 1
        else:
            print(f"You got it! The answer was {number}.")
            break
        
        if lives == 0:
            print(f"Oops! Game Over. The correct number was {number}.")

def main():
    while True:
        play_game()
        replay = input("Do you want to play again? Type 'y' or 'n': ").lower()
        if replay != 'y':
            print("Thanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    main()
