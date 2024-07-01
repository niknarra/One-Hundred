import data
import random

prevQuestion = 'defualt'
questionNum = 1
def generate_question():
    global prevQuestion, questionNum
    question = random.choice(data.question_data)
    questionText = question['text']

    while questionText == prevQuestion:
        question = random.choice(data.question_data)
        questionText = question['text']

    prevQuestion = questionText

    correctAnswer = question['answer']
    print(f"Q{questionNum}. {questionText}")
    questionNum += 1

    return correctAnswer
