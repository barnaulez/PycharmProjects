import requests
import os

class DataManager:

    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.sheety_key = os.environ.get("SHEETY_KEY")
        self.sheety_project = os.environ.get("SHEETY_PROJECT")
        self.sheet_name = os.environ.get("SHEET_NAME")
        self.token = os.environ.get("AUTH_TOKEN")

        self.header = {"Authorization": f"Bearer {self.token}"}

        self.sheety_endpoint = f"https://api.sheety.co/{self.sheety_key}/{self.sheety_project}/{self.sheet_name}"
        print(self.sheety_endpoint)
        self.details = {
            "destination": "",
            "iata_code": "",
            "price": 0
        }

    def get_flights(self):
        response = requests.get(url=self.sheety_endpoint, headers=self.header)
        response.raise_for_status()
        data = response.json()
        return data["prices"]

    def update_flights(self, flights: list):
        for flight in flights:
            endpoint = f"{self.sheety_endpoint}/{flight['id']}"
            body = {"price": flight}
            response = requests.put(url=endpoint, json=body, headers=self.header)
            response.raise_for_status()

    def get_iata(self, city_name):
        server = os.environ.get("KIWI_SERVER")
        locations_endpoint = os.environ.get("LOCATIONS_ENDPOINT")
        endpoint = f"{server}{locations_endpoint}"
        parameters = {
            "term": city_name,
            "location_types": "city",
            "limit": 1
        }
        header = {
            "apikey":os.environ.get("TEQUILA_KEY")
        }
        response = requests.get(url=endpoint, params=parameters, headers=header)
        response.raise_for_status()
        return response.json()["locations"][0]["code"]


