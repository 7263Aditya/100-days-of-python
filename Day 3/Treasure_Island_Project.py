print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

print("Where do you wanna go?\nType 'left' or 'right'.")
choice = input()
if choice == "left":
    print("There's a lake in front of you Type wait to wait for the boat or swim to swim across.")
    choice = input()
    if choice == "wait":
        print("You have arrived at other side of the lake unharmed. There is house with 3 doors.\nOne Red, one Yellow and one Blue. Which color do you wanna choose?")
        choice = input()
        if choice == "red":
            print("You caught up in the fire,you burned to death. You lose. Try Again.")
        elif choice == "yellow":
            print("You dropped down the hole under the carpet. You lose. Try Again.")
        elif choice == "blue":
            print("Congratulations! You found the treasure. You win!")
    elif choice == "swim":
        print("You were eaten by the crocodiles,You lose. Try Again.")
elif choice == "right":
    print("You fell into the hole. Try again.")