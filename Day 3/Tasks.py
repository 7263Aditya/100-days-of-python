# Control Flow
# If-else
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster.")
else:
    print("Sorry, you cannot ride the rollercoaster.")
    

# Modulo Operator
num = int(input("Enter a number: "))
if num % 2 == 0:
    print(f"{num} is an even number.")
else:
    print(f"{num}is an odd number.")
    

# Nesting and elif

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        print("Please pay $5.")
    elif age <= 18:
        print("Please pay $7")
    else:
        print("please pay $12.")
else:
    print("Sorry you have to grow taller before you can ride.")


# BMI Calculator
weight = 85
height = 1.85

bmi = weight / (height ** 2)

if bmi<18.5:
    print("underweight")
elif 18.5<bmi<25:
    print("normal weight")
else:
    print("overweight")
    

# Python Pizza    
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
bill = 0
if size == "S":
    bill = 15
elif size == "M":
    bill = 20
elif size == "L":
    bill = 25
else:
    print("You typed wrong inputs")

if pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is: ${bill}.")


# Logical Operators

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    elif age >=45 and age <= 55:
        print("Everything is going to be okay. Have a free ride on us.")
    else:
        bill = 12
        print("Adult tickets are $12.")

    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo == "Y":
        bill += 3

    print(f"Your final bill is ${bill}")

else:
    print("Sorry, you have to grow taller before you can ride.")


