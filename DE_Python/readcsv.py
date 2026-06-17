import csv

with open("new_data.csv","r") as file:
  reader=csv.reader(file)

  for row in reader:
    print(row)