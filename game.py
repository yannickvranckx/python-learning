import random

def guess_the_number():
    print("Welcome to 'Guess the number game!'")

    # Allow the player to choose difficulty
    while True:
        try:
            difficulty = int(input("Choose a difficulty level (1-Easy, 2-Medium, 3-Hard):"))
            if difficulty == 1:
                max_number = 50
                max_attempts = 10