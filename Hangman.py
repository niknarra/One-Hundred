# Day 7 - Jun 16 '24
# Hangman Game

import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

logo = r''' 
 _                                      
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''

print(logo)

lives = -1

word_list = ["aardvark", "baboon", "camel"]

word = random.choice(word_list)

dashes = []
guessedWord = []

for dash in word:
    dashes.append('_')
    guessedWord.append(' ')
    
print(' '.join(dashes))

while lives > -7: 
    if dashes == guessedWord:
        print (f"You got it! The word is {word}")
        break
    
    guessedLetter = str(input("Guess a Letter: "))
    
    if word.find(guessedLetter) != -1:
        for index, letter in enumerate(word):
            if guessedLetter == letter:
                dashes[index] = guessedLetter
                guessedWord[index] = guessedLetter
        print(' '.join(dashes))
        print("You got it Right. Keep going!\n")

    else:
        lives-=1
        print(stages[lives])
        print(f"You guessed {guessedLetter}, which is not right!\n")
        print(f"Lives remaining: {lives+7}\n")
      
if lives <= -7:  
    print(f"Game Over! The word was {word}.")
        