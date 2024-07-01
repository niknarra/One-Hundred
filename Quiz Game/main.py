import data
import question_model
import quiz_brain

print(data.logo)

while quiz_brain.game_continue:
    correctAnswer = question_model.generate_question()

    userAnswer = input("True or False? ")

    quiz_brain.check_answer(userAnswer, correctAnswer)
