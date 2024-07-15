# Day 34 - July 14 '24
# Quiz App with GUI

import html
import requests
from tkinter import *

THEME_COLOR = "#375362"

def getQuestions():
    questions = requests.get('https://opentdb.com/api.php?amount=10&type=boolean')
    questions.raise_for_status()
    questionsList = questions.json()
    return questionsList

def wrong(correctAns):
    global score
    if correctAns == 'False':
        score += 1
        canvas.itemconfig(score_text,text=f"Score:{score}")
    nextQues()

def right(correctAns):
    global score
    if correctAns == 'True':
        score += 1
        canvas.itemconfig(score_text,text=f"Score:{score}")
    nextQues()
    
def nextQues():
    canvas.itemconfig(question_text,text=ques)
    
    
questionsDump = getQuestions()
questions = {html.unescape(question['question']):question['correct_answer'] for question in questionsDump['results']}

window = Tk()
window.title("Quizzler")
window.minsize(width=400, height=600)
window.config(padx=50, pady=50,bg=THEME_COLOR)
canvas = Canvas(width=300, height=414)

score_text = canvas.create_text(150, 207, text="Score: 0", width=250, font=("Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=2)

question_text = canvas.create_text(150, 207, text="Hit me up!", width=250, font=("Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=0)

check_image = PhotoImage(file="right.png")
known_button = Button(image=check_image, highlightthickness=0,command=right)
known_button.grid(row=2, column=1)

cross_image = PhotoImage(file="wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0,command=wrong)
unknown_button.grid(row=2, column=0)

print(questions)

# for question in questions:
#     user_input = input(question)
#     if user_input == questions[question]:
#         print("Right!")
#     else:
#         print("Wrong!")