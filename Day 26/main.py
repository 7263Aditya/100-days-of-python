numbers = [1,2,3]
new_numbers = [n+1 for n in numbers]
name = "Aditya"
letter_list = [letter for letter in name]
range_list = [num*2 for num in range(1,5)]
names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]
# names
# ['Alex', 'Beth', 'Caroline', 'Dave', 'Elanor', 'Freddie']
short_names = [name for name in names if len(name)<5]
long_names = [name.upper() for name in names if len(name)>5]


# for loop

numbers = [1,2,3,4,5]
# new_list = []
# for n in numbers:
#     ad_1 = n+1
#     new_list.append(ad_1)
# print(new_list)

# List Comprehension    # new_list = [new_item for item in list]
new_list = [n+1 for n in numbers]
print(new_list)


name = "Angela"
letter_list =[letter for letter in name]
print(letter_list)

range_list = [num*2 for num in range(1,5)]
print(range_list)

names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]
import random
student_score ={student:random.randint(1,100) for student in names}

sentence = "What is the air-speed velocity of an unladen swallow?"
result = {word:len(word) for word in sentence.split()}
passed_students =  {student:score for (student,score) in student_score.items() if score >=60}

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24
}
# Dictionary Comprehension
weather_f = {day: (temp_c * 9/5) + 32 for (day, temp_c) in weather_c.items()}
print(weather_f)

student_dict = {"Student":["Angela","James","lily"],
                "Score":[56,76,98]}
# Looping through dict
for (key,value) in student_dict.items():
    print(value)

import pandas as pd
student_df = pd.DataFrame(student_dict)
print(student_df)

#Loop through a data frame
for (key,value) in student_df.items():
    print(value)

# loop through rows of the dataframe
for (index, row) in student_df.iterrows():
    if row.Student == "Angela":
        print(row.Score)