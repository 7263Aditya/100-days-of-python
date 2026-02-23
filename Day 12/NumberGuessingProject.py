import random
from art import logo

Easy_level_turns = 10
Hard_level_turns = 5

# Function to check the user against the actual answer
def check_Answer(user_input, answer,turns):
    if user_input > answer:
        print("Too high")
        return turns - 1
    elif user_input < answer:
        print("Too low")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}")
# function for setting the difficulty
def set_difficulty():
    game_level = input("Choose a difficulty level: Type 'easy' or 'hard': ")
    if game_level == "easy":
        return Easy_level_turns
    else:
        return Hard_level_turns
def game():
    # Choosing a random number between 1 and 100
    print(logo)
    print ("Welcome to the Number Guessing Project")
    print("I'm thinking of the number between 1 and 100")
    answer  = random.randint(1,100)
    print(answer)

    turns = set_difficulty()
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts left.")
        # Let the user guess the number
        guess = int(input("Guess the number between 1 and 100"))
        turns = check_Answer(guess, answer,turns)
        if turns == 0:
            print("You ran out of guesses, try again.")
            return
        elif guess != answer:
            print("Guess again")
    
game()