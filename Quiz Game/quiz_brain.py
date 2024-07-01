userScore = 0


def check_answer(userAnswer, correctAnswer):
    global userScore
    if userAnswer == correctAnswer:
        userScore += 1
        print("You're Right!")
    else:
        print("You're Wrong!")

    print(f"Your Current Score: {userScore}\n")