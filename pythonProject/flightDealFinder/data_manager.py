import requests

SHEETY_KEY = "c6ed8e1a6d1f0e75100e69bf16f6f335"
SHEETY_PROJECT = "flightDeals"
SHEET_NAME = "prices"
BEARER_TOKEN = "adkjgbfsdfgıytqw43rfgqkvfhgalwu34ygvkhasdcasdgafsf"
SHEETY_ENDPOINT = f"https://api.sheety.co/{SHEETY_KEY}/{SHEETY_PROJECT}/{SHEET_NAME}"

header = {"Authorization": f"Bearer {BEARER_TOKEN}"}

#class DataManager:
#    #This class is responsible for talking to the Google Sheet.
#    def __init__(self):
#        self.details = {
#            "destination": "",
#            "iata_code": "",
#            "price": 0
#        }

def get_flights():
    response = requests.get(url=SHEETY_ENDPOINT)
    response.raise_for_status()
    data = response.json()
    print(data)

get_flights()