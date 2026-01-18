import pandas as pd

# Read CSV
data = pd.read_csv("./Pandas_Practice/sample_data.csv")

# Type checks
print(type(data))
print(type(data["temp"]))

# Convert DataFrame to dictionary
data_dict = data.to_dict()
print(data_dict)

# Convert Series to list
temp_list = data["temp"].to_list()
print(temp_list)

# Average temperature (using Python)
average_temp = sum(temp_list) / len(temp_list)
print(average_temp)

# Average temperature (using pandas)
print(data["temp"].mean())

# Maximum temperature
print(data["temp"].max())

# Get a column
print(data["condition"])
print(data.condition)

# Get row where day is Monday
monday = data[data.day == "Monday"]
print(monday)

# Get row with maximum temperature
max_temp_row = data[data.temp == data.temp.max()]
print(max_temp_row)

# Get Monday condition
print(monday.condition)

# Monday temperature in Fahrenheit
monday_temp_f = monday.temp.iloc[0] * 9 / 5 + 32
print(monday_temp_f)

# Create DataFrame from dictionary
student_dict = {"students": ["Amy", "James", "Angela"], "scores": [76, 56, 65]}
student_data = pd.DataFrame(student_dict)
print(student_data)

# Save DataFrame to CSV
student_data.to_csv("./Pandas_Practice/new_data.csv")
