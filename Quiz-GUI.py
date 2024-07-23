# Day 34 - July 14 '24
# Quiz App with GUI
import requests
from tkinter import *
import html

THEME_COLOR = "#375362"
score = 0
current_question = 0

def getQuestions():
    questions = requests.get('https://opentdb.com/api.php?amount=10&type=boolean')
    questions.raise_for_status()
    questionsList = questions.json()
    return questionsList

def get_high_score():
    try:
        with open("high_score.txt", "r") as file:
            return int(file.read())
    except FileNotFoundError:
        return 0

def update_high_score(new_score):
    current_high_score = get_high_score()
    if new_score > current_high_score:
        with open("high_score.txt", "w") as file:
            file.write(str(new_score))
        return new_score
    return current_high_score

questionsDump = getQuestions()
questions = [html.unescape(question['question']) for question in questionsDump['results']]
answers = [question['correct_answer'] for question in questionsDump['results']]

def display_question():
    global current_question
    if current_question < len(questions):
        canvas.itemconfig(question_text, text=questions[current_question])
    else:
        canvas.itemconfig(question_text, text="Quiz completed!")
        known_button.config(state="disabled")
        unknown_button.config(state="disabled")

def check_answer(user_answer):
    global score, current_question
    if current_question < len(questions):
        if user_answer == answers[current_question]:
            score += 1
        current_question += 1
        canvas.itemconfig(score_text, text=f"Score: {score}")
        display_question()
    if current_question == len(questions):
        new_high_score = update_high_score(score)
        canvas.itemconfig(high_score_text, text=f"High Score: {new_high_score}")

def right():
    check_answer('True')

def wrong():
    check_answer('False')

window = Tk()
window.title("Quizzler")
window.minsize(width=400, height=600)
window.config(padx=50, pady=50, bg=THEME_COLOR)

canvas = Canvas(width=300, height=250)
canvas.grid(row=1, column=0, columnspan=2, pady=50)

question_text = canvas.create_text(150, 125, width=280, text="", font=("Arial", 20, "italic"), fill=THEME_COLOR)
score_text = canvas.create_text(150, 25, text="Score: 0", font=("Arial", 16, "normal"), fill=THEME_COLOR)
high_score_text = canvas.create_text(150, 50, text=f"High Score: {get_high_score()}", font=("Arial", 16, "normal"), fill=THEME_COLOR)

check_image = PhotoImage(file="right.png")
known_button = Button(image=check_image, highlightthickness=0, command=right)
known_button.grid(row=2, column=1)

cross_image = PhotoImage(file="wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command=wrong)
unknown_button.grid(row=2, column=0)

display_question()

window.mainloop()