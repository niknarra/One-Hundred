# Day 29 - July 9 '24
# Password Manager

from tkinter import *
import random

# Define the symbols and letters
symbols = ['~', '`', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '+', '=', '{', '[', '}', ']', '|', ':', ';', '<', '>', '?']
letters = [chr(i) for i in range(97, 123)] + [chr(i) for i in range(65, 91)]

# Function to generate a random password
def generate():
    totalLen = random.randint(12, 14)

    numOfLetters = random.randint(1, totalLen - 2)
    numOfSymbols = random.randint(1, totalLen - numOfLetters - 1)
    numOfNums = totalLen - numOfLetters - numOfSymbols

    password = []

    for _ in range(numOfLetters):
        password.append(random.choice(letters))

    for _ in range(numOfSymbols):
        password.append(random.choice(symbols))

    for _ in range(numOfNums):
        password.append(str(random.randint(0, 9)))

    random.shuffle(password)
    finalPwd = ''.join(password)

    pwdEntry.delete(0, END)
    pwdEntry.insert(0, finalPwd)

# Function to add the password entry to the file
def add():
    pwd = pwdEntry.get()
    with open('pwd.txt', mode='a') as file:
        file.writelines(f"{siteEntry.get()} | {emailEntry.get()} | {pwd}\n")
    print("Added")

    siteEntry.delete(0, END)
    emailEntry.delete(0, END)
    pwdEntry.delete(0, END)

# Create the main window
window = Tk()
window.title("Password Manager")
window.minsize(width=500, height=450)
window.config(padx=50, pady=50)

# Row 1: Logo
canvas = Canvas(width=200, height=224, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 112, image=logo_img)
canvas.grid(column=1, row=0, columnspan=3)

# Row 2: Website entry and label
sitelabel = Label(text='Website ', font=('Arial', 15))
sitelabel.grid(row=1, column=0)
siteEntry = Entry(width=35)
siteEntry.grid(row=1, column=1, columnspan=2, pady=5)

# Row 3: Email/Username entry and label
emailLabel = Label(text='Email/Username ', font=('Arial', 15))
emailLabel.grid(row=2, column=0)
emailEntry = Entry(width=35)
emailEntry.grid(row=2, column=1, columnspan=2, pady=5)

# Row 4: Password entry and label
pwdLabel = Label(text='Password ', font=('Arial', 15))
pwdLabel.grid(row=3, column=0)
pwdEntry = Entry(width=21)
pwdEntry.grid(row=3, column=1, pady=5)

genButton = Button(text='Generate!', command=generate)
genButton.grid(row=3, column=2, padx=5)

# Row 5: Add button
addButton = Button(text='Add!', command=add)
addButton.grid(row=4, column=1, columnspan=2, pady=5)

# Start the Tkinter event loop
window.mainloop()
