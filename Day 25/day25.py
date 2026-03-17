# import csv

# with open("weather_data.csv") as csv_file:
#     data = csv_file.readlines()

# with open("weather_data.csv") as csv_file:
#     data = csv.reader(csv_file)
#     temps = []
#     for row in data:
#         if row[1] != "temp":
#             temps.append(int(row[1]))
#     print(temps)

# import pandas as pd

# data = pd.read_csv('weather_data.csv')
# # print(data)
# print(type(data)) # this will print the pandas dataframe
# # print(data['temp'])
# print(type(data['temp']))   # this will print the pandas series
# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data['temp'].to_list()
# print(temp_list)
#
# avg_temp = sum(temp_list) / len(temp_list)
# print(avg_temp)
# # OR
# print(data['temp'].mean())
#
# print(data['temp'].max())
#
#
# print(data['condition'])
# #OR
# print(data.condition)
#
# # Get data from the rows
# print(data[data.day=='Monday'])
# print(data[data.temp == data.temp.max()])
#
# monday = data[data.day=='Monday']
# monday_temp = monday.temp[0]
# monday_temp_f = monday_temp * 9/5 + 32
# print(monday_temp_f)
#
#
# # create a dataframe from scratch
# data_dict = {
#     "students":["Amy","James","Angela"],
#     "scores":[76, 56, 65]
# }
# data = pd.DataFrame(data_dict)
# data.to_csv('new_data.csv')

import pandas as pd
data = pd.read_csv('Squirrel_Data.csv')
print(data[data['Primary Fur Color'] == "Gray"])
print(data[data['Primary Fur Color'] == "Cinnamon"])
print(data[data['Primary Fur Color'] == "Black"])


# count of squirrels
gray_sq_cnt = len(data[data['Primary Fur Color'] == "Gray"])
red_sq_cnt = len(data[data['Primary Fur Color'] == "Cinnamon"])
blk_sq_cnt = len(data[data['Primary Fur Color'] == "Black"])

data_dict = {
    "Fur color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_sq_cnt, red_sq_cnt, blk_sq_cnt]
}

# print(pd.DataFrame(data_dict)
df = pd.DataFrame(data_dict)
df.to_csv('Squirrel_count.csv')