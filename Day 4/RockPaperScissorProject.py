rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random
imgs = [rock,paper,scissors]

user_choice = int(input("What do you choose?, Type 0 for Rock, Type 1 for Paper, Type 2 for Scissors.\n"))
if user_choice >= 0 and user_choice <= 2:
    print(imgs[user_choice])

computer_choice = random.randint(0,2)
print("computer chose:")
print(imgs[computer_choice])
if user_choice>=3 or user_choice < 0:
    print("You type and invalid number. Try Again.")
elif user_choice == 0 and computer_choice == 2:
    print("You win!")
if computer_choice == 0 and user_choice == 2:
    print("You lose!")
elif computer_choice > user_choice:
    print("You lose!")
elif user_choice > computer_choice:
    print("You win!")
elif computer_choice == user_choice:
    print("Its a draw!")