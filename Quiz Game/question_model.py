import data
import random
import quiz_brain

questionNum = 1
currentQuestionIndex = 0

questionsList = data.question_data
random.shuffle(questionsList)

totalQuestions = len(data.question_data)
game_continue = True


def generate_question():
    global currentQuestionIndex, questionNum, game_continue

    if currentQuestionIndex >= totalQuestions:
        print("No more questions available. The quiz has ended.")
        print(f"Your Final Score: {quiz_brain.userScore}")
        game_continue = False
        return None

    question = questionsList[currentQuestionIndex]
    currentQuestionIndex += 1

    questionText = question['text']
    correctAnswer = question['answer']

    print(f"Q{questionNum}. {questionText}")

    questionNum += 1
    return correctAnswer
