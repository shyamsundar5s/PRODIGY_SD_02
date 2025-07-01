import random

def guessing_game():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    
    # Initialize variables
    attempts = 0
    guess = None

    print("Welcome to the Guessing Game!")

    while guess != secret_number:
        try:
            # Prompt the user to input their guess
            guess = int(input("Enter your guess (between 1 and 100): "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        # Increment the number of attempts
        attempts += 1

        # Compare the guess to the secret number
        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the correct number {secret_number} in {attempts} attempts.")

if __name__ == "__main__":
    guessing_game()
