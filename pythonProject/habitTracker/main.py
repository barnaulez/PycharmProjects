import requests
from datetime import datetime, timedelta
USERNAME = "brnman22"
TOKEN = "TOKEN"
GRAPHID = "ID"
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": "TOKEN",
    "username": "brnman22",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

#response = requests.post(url=pixela_endpoint, json=user_params)
#print(response.text)
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"


graph_config = {
    "id": "brnman01",
    "name": "Read Pages graph",
    "unit": "Pages",
    "type": "int",
    "color": "sora",
    "timezone": "Asia/Istanbul"

}

headers = {
    "X-USER-TOKEN": TOKEN
}



today = datetime.now()
yesterday = today - timedelta(days=1)
print(yesterday)

pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}/{yesterday.strftime('%Y%m%d')}"

pixel_conf = {
    "date": yesterday.strftime("%Y%m%d"),
    "quantity": "118"
}

#response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
#print(response.text)

response = requests.put(url=pixel_endpoint, json=pixel_conf, headers=headers)
print(response.text)
