# Day 11 - Jun 20 '24
# Blackjack Game

import os
import random

logo = r'''
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _' |/ __| |/ / |/ _' |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
'-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\
      |  \/ K|                            _/ |                
      '------'                           |__/           
'''

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
    return random.choice(cards)

def check_score(playerScore, compScore):
    if playerScore == 21:
        print("You win via Blackjack!")
        return False
    if playerScore > 21:
        print(f"Your cards: {player}, current score: {playerScore}")
        print("You went over. You lose 😭")
        return False
    if compScore == 21:
        print("Computer wins with Blackjack!")
        return False
    if compScore > 21:
        print(f"Computer's cards: {computer}, current score: {compScore}")
        print("Computer went over. You Win!")
        return False
    return True

loop = True

while loop:
    start = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

    if start == 'y':
        print(logo)
        game = True
        player = [deal_card(), deal_card()]
        computer = [deal_card(), deal_card()]
    elif start == 'n':
        loop = False
        continue

    while game:
        playerScore = sum(player)
        compScore = sum(computer)
        print(f"Your cards: {player}, current score: {playerScore}")
        print(f"Computer's first card: {computer[0]}")
        game = check_score(playerScore, compScore)
        if not game:
            break

        hit = input("Type 'y' to get another card, type 'n' to pass: ")
        if hit == 'y':
            player.append(deal_card())
            playerScore = sum(player)
            game = check_score(playerScore, compScore)
            if not game:
                break
        else:
            while compScore < 17:
                computer.append(deal_card())
                compScore = sum(computer)
                game = check_score(playerScore, compScore)
                if not game:
                    break
            game = False

    print(f"Your final hand: {player}, final score: {playerScore}")
    print(f"Computer's final hand: {computer}, final score: {compScore}")

    if playerScore <= 21 and compScore <= 21:
        if playerScore > compScore:
            print("You win!")
        elif playerScore < compScore:
            print("You lose.")
        else:
            print("It's a draw.")
