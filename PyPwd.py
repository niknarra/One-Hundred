# Day 5 - Jun 15 '24
# PyPassword Generator

import random

symbols = ['~','`','!','@','#','$','%','^','&','*','(',')','_','-','+','=','{','[','}',']','|',':',';','<','>','?']

letters = [chr(i) for i in range(97, 123)] + [chr(i) for i in range(65, 91)]

print(letters)

print("Welcome to the PyPassword Generator!")

numOfLetters = int(input("How many letters would you like in your password?\n"))

numOfSymbols = int(input("How many symbols would you like?\n"))

numOfNums = int(input("How many numbers would you like?\n"))

totalLen = numOfLetters+numOfNums+numOfSymbols

password = []


for _ in range(numOfLetters):
    password.append(random.choice(letters))

for _ in range(numOfSymbols):
    password.append(random.choice(symbols))

for _ in range(numOfNums):
    password.append(str(random.randint(0, 9)))
    
random.shuffle(password)

finalPwd = ''.join(password)

print(f"Your password could be: {finalPwd}")