# FilenotFoundError
# with open("a_file.txt", "r") as a_file:
#     file.read()

# KeyError
# a_dict = {"key": "value"}
# value =a_dict["non-existent_key"]

# IndexError
# fruit_list = ['Apple',"Banana","Pear"]
# fruit = fruit_list[3]

# TypeError
# text = "abcdefg"
# print(text+3)

# try catch method
# try:
#     file = open("a_file.txt")
#     a_dict = {"key": "value"}
#     print(a_dict['key'])
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("something")
# except KeyError as error_message:
#     print(f"that key {error_message} doesnt exist")
#
# else:
#     content = file.read()
#     print(content)
# finally:
#     raise TypeError("This is the error message")

height = float(input("height"))
weight = float(input("weight"))

if height is 3:
    raise ValueError("human height should nto exceed 3 meters.")

bmi = weight / (height * height)
print(bmi)