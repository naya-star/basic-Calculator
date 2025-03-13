# 2. Simple Quiz Game 🎮
def quiz_game():
    score = 0
    print("Welcome to the Python Quiz!")

    answer = input("What data type is used to store text in Python? ")
    if answer.lower() == "string":
        print("Correct!")
        score += 1
    else:
        print("Wrong answer!")

    answer = input("Which keyword is used to define a function? ")
    if answer.lower() == "def":
        print("Correct!")
        score += 1
    else:
        print("Wrong answer!")

    print(f"Your final score is: {score}/2")

    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() == "yes":
        quiz_game()

quiz_game()
