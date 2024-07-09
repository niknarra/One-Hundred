# Day 27 - July 8 '24
# Miles to Kilometers converter with Tkinter

from tkinter import *

window = Tk()
window.title('Miles to Kilometers')
window.minsize(width=300, height=150)
window.config(padx=20, pady=20)

def button_click():
  miles = int(milesEntry.get())
  kms = miles * 1.609
  kmsText.config(text=kms)

# Row 1: Entry and label for miles
milesEntry = Entry(width=10)
milesEntry.grid(row=1, column=2)
mileslabel = Label(text='Miles', font=('Arial', 15, 'italic'))
mileslabel.grid(row=1, column=3)

# Row 2: Text "is equal to" and result display for kilometers
helpText = Label(text='is equal to', font=('Arial', 15, 'italic'))
helpText.grid(row=2, column=1)

kmsText = Label(text='0', font=('Arial', 15, 'italic'))
kmsText.grid(row=2, column=2)

kmslabel = Label(text='Km', font=('Arial', 15, 'italic'))
kmslabel.grid(row=2, column=3)

# Row 3: Calculate button
button = Button(text='Calculate!', command=button_click)
button.grid(row=3, column=2)

window.mainloop()