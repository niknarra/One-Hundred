userScore = 0
game_continue = True


def check_answer(userAnswer, correctAnswer):
    global userScore, game_continue
    if userAnswer == correctAnswer:
        userScore += 1
        print("You're Right!")
        print(f"Your Current Score: {userScore}\n")
        game_continue = True
    else:
        print("You're Wrong! Game Over")
        print(f"Your Final Score: {userScore}")
        game_continue = False
