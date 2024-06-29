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
            elif difficulty == 2:
                max_number = 100
                max_attempts = 7
            elif difficulty == 3:
                max_number = 200
                max_attempts = 5
            else:
                print("Invalid choice. Please choose 1, 2, or 3.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")

    number_to_guess = random.randint(1, max_number)
    attempts = 0
    guessed = False

    print(f"I'm thinking of a number between 1 and {max_number}. You gave {max_attempts} attempts.")

    while not guessed and attempts < max_attempts:
        try:
            guess = int(input("Take a guess:"))
            attempts += 1

            if guess < number_to_guess:
                print("Your guess is too low.")
            elif guess > number_to_guess:
                print("Your guess is too high.")
            else:
                guessed = True
                print(f"Good job! You guessed my number in {attempts} attempts.")
        except ValueError:
            print("Please enter a valid integer.")

    if not guessed:
        print(f"Sorry, you've used all your attempts. The number was {number_to_guess}.")

    # Ask if the player wants to play again
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == 'yes':
        guess_the_number()

if __name__ == "__main__":
    guess_the_number()                  
