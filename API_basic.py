import requests

response = requests.get("http://api.open-notify.org/iss-now.json")

print(response)

data = response.json()["iss_position"]

print(data)
