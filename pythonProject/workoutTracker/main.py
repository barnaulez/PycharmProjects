import requests
from datetime import datetime

#.nutritionix.com API
API_ID = "831a100e"
API_KEY = "fa0265cc0b7611325e0e26a3e12eef82"
SHEETY_KEY = "c6ed8e1a6d1f0e75100e69bf16f6f335"
SHEETY_PROJECT = "myWorkouts"
SHEET_NAME = "workouts"
BEARER_TOKEN = "a;kjhflausfghaiuwreypqui;afhbns.jkgbnas;kfgdjlnagdf[8y5-9834hnfg;kdsav"

nutrionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = f"https://api.sheety.co/{SHEETY_KEY}/{SHEETY_PROJECT}/{SHEET_NAME}"
nutrionix_headers = {
    "x-app-id": API_ID,
    "x-app-key": API_KEY
}

exercises = input("Tell me which exercises you did: ")

exercises_input = {
    "query": exercises,
    "gender": "male",
    "weight_kg": 88.5,
    "height_cm": 176,
    "age": 40
}

response = requests.post(url=nutrionix_endpoint, json=exercises_input, headers=nutrionix_headers)
print(response.text)
calories = response.json()

sheety_header = {"Authorization": f"Bearer {BEARER_TOKEN}"}
today = datetime.now()
for calory in calories["exercises"]:
    body = {
        "workout":{
            "date": today.strftime("%d/%m/%Y"),
            "time": today.strftime("%H:%M:%S"),
            "exercise": calory["name"].capitalize(),
            "duration": calory["duration_min"],
            "calories": calory["nf_calories"]
        }
    }
    response = requests.post(url=sheety_endpoint, json=body, headers=sheety_header)
    print(response)
