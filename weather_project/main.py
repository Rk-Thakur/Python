# with open('weather_data.csv') as data_file:
#     data = data_file.readlines()
#     print(data)


# import csv

# with open('weather_data.csv') as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
#     print(temperatures)


import pandas
# data = pandas.read_csv('weather_data.csv')
# print(type(data))
# print(data['temp'])
# print(data.to_dict())

# temp_list = data['temp'].to_list()
# print(len(temp_list))

# average = sum(temp_list) / len(temp_list)
# print(average)

# print(data['temp'].mean())

# print(data[data.day == 'Monday'])
# print(data[data.condition == 'Sunny'])

# monday= (data[data.day == 'Monday'])
# print(monday.temp * 10)

#Create a dataframe from scratch
data_dict = {
    'students': ['any','jack'],
    'scores' : [23,25]
}

data = pandas.DataFrame(data_dict)
data.to_csv('new_data.csv')
print(data)
