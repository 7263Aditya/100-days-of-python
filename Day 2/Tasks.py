# Data Types
# Subscripting
print("Hello"[0])

# String
"123"
print("123" + "345")

# Integer = Whole number
print(123 + 345)

# Large Integers
print(123_456_789)

# Float = Floating Point Number
print(3.14159)

# Boolean
print(True)
print(False)


# TypeError,checking and conversion
print(len("12345"))

print(type("Hello"))
print(type(1234))
print(type(12.34))
print(type(True))

print("Number of letters in your name: " + str(len(input("Enter your name"))))


username = input("Enter your name:")
len_username = len(username)

print(type("number of letter in your username: ")) # str
print(type(len_username)) # int

print("Number of letters in your username: " + str(len_username))

# Mathematical Operations
print("My age: " + str(12))
print(123 + 456)
print(7 - 3)
print(3 * 2)
print(5 / 3)
print(5 // 3)
print(2 ** 3)

# PEMDASLR Order
# ()
# **
# * OR /
# + OR -

# Outputs 7
print(3 * 3 + 3 / 3 - 3)

# Outputs 3
print(3 * (3 + 3) / 3 - 3)


# Number Manipulation
bmi = 105 / 1.67 ** 2
print(bmi)

print(int(bmi))

print(round(bmi))
print(round(bmi, 2))

score = 0

# User scores a point
score += 1
print(score)

# f-strings
print("Your score is " + str(score))


score = 0
height = 1.8
is_winning =True

print(f"your score is =  {score}, your height is = {height}, you are winning is {is_winning}")


