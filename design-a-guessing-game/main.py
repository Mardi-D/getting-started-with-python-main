#Guess Game - SK
import random

# Generate a random number between 0 and 100 (inclusive)
random_number = random.randrange(101)

correct_guess = False

# Loop until the correct guess is made
while not correct_guess:
    user_input = input("Guess a number between 0 and 100: ")

    try:
        # Try to convert user input to an integer
        number = int(user_input)
        
        # Check if the guess is correct
        if number == random_number:
            correct_guess = True
        elif number > random_number:
            print("You guessed too high!")
        elif number < random_number:
            print("You guessed too low!")
    except ValueError:
        # Handle case where the input is not a valid number
        print("Please enter a number :)")

# Once the correct guess is made, print the success message
print("You guessed the right number!")