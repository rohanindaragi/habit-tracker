# importing the modules
import requests
from datetime import datetime

#Username
USERNAME = "rohanvi"
TOKEN = "hjkh34h3jk4hj34h3jh4"
GRAPH_ID = "graph1"

# URL endpoint
pixela_endpoint = "https://pixe.la/v1/users"

# parameters of the users
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# graph endpoint
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

# graph configuration
graph_config = {
    "id": GRAPH_ID,
    "name": "Coding Graph",
    "unit": "Hour",
    "type": "float",
    "color": "ajisai"
}

# headers
headers = {
    "X-USER-TOKEN": TOKEN
}
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# endpoint for pixel creation
pixela_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()
print(today.strftime("%Y%m%d"))

pixel_data = {
    # to create the own format for date
    "date": today.strftime("%Y%m%d"),  # year/month/date format
    "quantity": input("How many hours did you spend for coding today?"),
}

response = requests.post(url=pixela_creation_endpoint, json=pixel_data, headers=headers)
print(response.text)

# endpoint for update
update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

new_pixel_data = {
    "quantity": "4.5"
}

# request for update
# response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
# print(response.text)

# endpoint for delete
delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)