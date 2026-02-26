# Display art
from art import logo,vs
from game_data import data
import random

# format the account data into the printable format
def format_data(account):
    """format the account data into the printable format."""
    acc_name =account["name"]
    acc_desc =account["description"]
    acc_country =account["country"]
    return f"{acc_name}, a {acc_desc}, from {acc_country}"

# - User if statement to check if user is correct
def check_answer(user_guess, a_follower_cnt, b_follower_cnt):
    """Takes user guess and checks whether they are correct."""
    if a_follower_cnt > b_follower_cnt:
        return user_guess == "a"
    else:
        return user_guess == "b"


print(logo)
score = 0
game_should_continue = True
acc_b =random.choice(data)

# Make the game repeatable
while game_should_continue:
    # Generate random account from the game data
    # Making account at position B become the next account at position A
    acc_a = acc_b
    acc_b = random.choice(data)
    if acc_a == acc_b:
        acc_b = random.choice(data)

    print(f"Compare A:{format_data(acc_a)}.")
    print(vs)
    print(f"Against B:{format_data(acc_b)}.")

    # ask users for a guess
    guess = input("Who has more followers? Type 'A' or 'B'.").lower()

    # Clear the screen
    print("\n" * 20)
    print(logo)

    # Check if user is correct
    # - Get follower count of each account
    a_follower_cnt = acc_a["follower_count"]
    b_follower_cnt = acc_b["follower_count"]
    is_correct = check_answer(guess, a_follower_cnt, b_follower_cnt)

    # Give user feedback on their guess.
    # Score keeping

    if is_correct:
        score += 1
        print(f"You are right!,Current score: {score}")
    else:
        print(f"Sorry, you are wrong! Final Score: {score}")
        game_should_continue = False
        