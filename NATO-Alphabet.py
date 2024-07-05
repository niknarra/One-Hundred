# Day 26 - July 5 '24
# NATO Alphabet Project

import pandas

Nato = pandas.read_csv('nato_phonetic_alphabet.csv')

Nato_Dict = {row.letter:row.code for (index,row) in Nato.iterrows()}
# print(Nato_Dict['K'])

word = input("Enter a Word: ").upper()

#word_list = list(word.upper())

nato_list = [Nato_Dict[letter] for letter in word]

print(nato_list)

