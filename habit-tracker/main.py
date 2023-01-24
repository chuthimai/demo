import requests
import datetime as dt

pixela_endpoint = "https://pixe.la/v1/users"
USERNAME = "mai3723"
TOKEN = "weshouldreadbookeveryday"

# Create an account
user_param = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_param)
# print(response.text)

# Create a graph
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

headers = {
    "X-USER-TOKEN": TOKEN
}

graph_config = {
    "id": "graph1",
    "name": "Coding Graph",
    "unit": "hours",
    "type": "float",
    "color": "ajisai"
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# Create a pixel
pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1"

today = dt.datetime.today()
today = today.strftime("%Y%m%d")

pixel_config = {
    "date": today,
    "quantity": "2.5"
}

# response = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)
# print(response.text)

pixel_put_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1/{today}"

new_pixel_data = {
    "quantity": "1.5"
}

response = requests.put(url=pixel_put_endpoint, json=new_pixel_data, headers=headers)
print(response.text)

# Delete pixel
# response = requests.delete(url=pixel_put_endpoint, headers=headers)
# print(response.text)


