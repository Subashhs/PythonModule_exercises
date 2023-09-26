import random

# Generate a random number between 1 and 10
secret_number = random.randint(1, 10)

# Initialize a variable to keep track of the number of guesses
attempts = 0

while True:
    # Get user's guess
    user_guess = int(input("Guess the number between 1 and 10: "))

    # Increment the number of attempts
    attempts += 1

    # Check if the guess is correct
    if user_guess == secret_number:
        print(f"Correct! You guessed the number in {attempts} attempts.")
        break
    elif user_guess < secret_number:
        print("Too low. Try again.")
    else:
        print("Too high. Try again.")
