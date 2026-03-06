import requests
from datetime import datetime

TOKEN = "kaisbdhbfcfurffidfiedndf"

USER_NAME = "ramse"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token":TOKEN,
    "username":USER_NAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes",

}

# response = requests.post(url=pixela_endpoint,json=user_params)

# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs"

graph_params = {
       "id":"graph1",
       "name":"cycling Graph",
       "unit":"km",
       "type":"float",
       "color":"ajisai"
}

headers = {
    "X-USER-TOKEN":TOKEN
}

# response =requests.post(url=graph_endpoint,json=graph_params,headers=headers)

# print(response.text)

# https://pixe.la/v1/users/ramse/graphs/graph1.html = URL to check graph

pixel_creation_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/graph1"

today = datetime.now()


pixel_params = {
    "date":today.strftime("%Y%m%d"),
     "quantity":"9.75"
}


# response = requests.post(url=pixel_creation_endpoint,json=pixel_params,headers=headers)

# print(response.text)


update_endpoint = (
    f"{pixela_endpoint}/{USER_NAME}/graphs/graph1/{today.strftime("%Y%m%d")}"
)

headers = {"X-USER-TOKEN": TOKEN}

update_data = {"quantity": "10"}  # new value

# response = requests.put(url=update_endpoint, json=update_data, headers=headers)

# print(response.text)


delete_endpoint = (
    f"https://pixe.la/v1/users/{USER_NAME}/graphs/graph1/{today.strftime("%Y%m%d")}"
)

headers = {"X-USER-TOKEN": TOKEN}

response = requests.delete(url=delete_endpoint, headers=headers)

print(response.text)
