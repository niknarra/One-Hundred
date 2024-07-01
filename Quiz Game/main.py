import data
import question_model
import quiz_brain

print(data.logo)

while question_model.game_continue:
    correctAnswer = question_model.generate_question()

    if not question_model.game_continue:
        break

    userAnswer = input("True or False? ")

    quiz_brain.check_answer(userAnswer, correctAnswer)
