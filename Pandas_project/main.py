# with open("./Pandas_project/weather_data.csv") as weather_file:
#     data = weather_file.readlines()
#     print(data)

# import csv

# with open("./Pandas_project/weather_data.csv") as weather_file:
#     data = csv.reader(weather_file)

#     temperature = []
#     for row in data:
#         if row[1] != "temp":
#             temperature.append(int(row[1]))
    
#     print(temperature)


import pandas

data = pandas.read_csv("./Pandas_project/weather_data.csv")

print(data)
