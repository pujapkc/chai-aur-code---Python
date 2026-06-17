# import json
# import csv

# # Load JSON file
# with open('data.json', 'r') as f:
#     data = json.load(f)

# # If JSON is a list of dictionaries
# with open('data.csv', 'w', newline='') as f:
#     writer = csv.DictWriter(f, fieldnames=data[0].keys())
#     writer.writeheader()
#     writer.writerows(data)

# import pandas as pd

# df=pd.read_json('data.json')

# df.to_csv('data.csv' index=False)