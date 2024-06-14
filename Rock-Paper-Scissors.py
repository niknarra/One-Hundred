# Day 4 - Jun 9 '24
# Rock Paper Scissors

import random

userChoice = int(input(("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")))

choices = {0:'Rock',1:'Paper',2:'Scissors'}

compChoice = random.randrange(0,2)

if userChoice == compChoice:
    print(f"We both chose {choices[userChoice]}. It's a Draw!")
elif userChoice == 2 and compChoice == 0:
    print(f"I chose {choices[compChoice]}. You Lost!")
elif userChoice == 0 and compChoice == 2:
    print(f"I chose {choices[compChoice]}. You Won!")
elif userChoice > compChoice:
    print(f"I chose {choices[compChoice]}. You Won!")
elif userChoice < compChoice:
    print(f"I chose {choices[compChoice]}. You Lost!")

# if userChoice==0:
#     if compChoice == 'Rock':
#         print("I chose Rock. It's a Draw!")
#     elif compChoice == 'Scissors':
#         print("I chose Scissors. You Win!")
#     else:
#         print("I chose Paper. You Lost!")
# elif userChoice==1:
#     if compChoice == 'Rock':
#         print("I chose Rock. You Won!")
#     elif compChoice == 'Scissors':
#         print("I chose Scissors. You Lost!")
#     else:
#         print("I chose Paper. It's a Draw!")
# else:
#     if compChoice == 'Rock':
#         print("I chose Rock. You Lost!")
#     elif compChoice == 'Scissors':
#         print("I chose Scissors. It's a Draw!")
#     else:
#         print("I chose Paper. You Won!")
