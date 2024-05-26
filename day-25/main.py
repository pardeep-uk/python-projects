# # with open("C:/Users/pardeep.singh02/Desktop/python-projects/python-projects/python-projects/day-25/weather_data.csv") as data_file:
# #     data = data_file.read()
# #     print(data)
    
# # import csv

# # with open("C:/Users/pardeep.singh02/Desktop/python-projects/python-projects/python-projects/day-25/weather_data.csv") as data_file:
# #     data = csv.reader(data_file)
# #     temperatures = []
# #     for row in data:
# #         if row[1] != "temp":
# #            temperatures.append(row[1])
# #     print(temperatures)

# import pandas

# data = pandas.read_csv("C:/Users/pardeep.singh02/Desktop/python-projects/python-projects/python-projects/day-25/weather_data.csv")
# type(data)
# # print(data['temp'])

import pandas


data = pandas.read_csv("C:/Users/pardeep.singh02/Desktop/python-projects/python-projects/python-projects/day-25/2018_Central_Park_Squirrel_Census_Squirrel_Data.csv")
grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
# print(grey_squirrels_count)
# print(red_squirrels_count)
# print(black_squirrels_count)

data_dict = {
    "Fur Color": ["Gray","Red","Black"],
    "Squirrels_Count": [grey_squirrels_count,red_squirrels_count,black_squirrels_count]
}

# print(pandas.DataFrame(data_dict))
pandas.DataFrame(data_dict).to_csv("C:/Users/pardeep.singh02/Desktop/python-projects/python-projects/python-projects/day-25/squirrel_count.csv")