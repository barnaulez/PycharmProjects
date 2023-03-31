import os
import requests
from pprint import pprint
from datetime import datetime

class FlightSearch:
    def __init__(self, from_iata):
        self.from_iata = from_iata
        self.server = os.environ.get("KIWI_SERVER")
        self.search_endpoint = os.environ.get("SEARCH_ENDPOINT")
        self.endpoint = f"{self.server}{self.search_endpoint}"

    def flight_search(self, dateFrom, dateTo, fly_to):
#        print(dateFrom, dateTo, fly_to)

        parameters = {
            "fly_from": f"city:{self.from_iata}",
            "fly_to": f"city:{fly_to}",
            "date_from": dateFrom,
            "date_to": dateTo,
            "flight_type": "oneway",
            "ret_from_diff_city": "false",
            "ret_to_diff_city": "false",
            "selected_cabins": "M",
            "max_stopovers": 1,
            "limit": 1
        }
        header = {
            "apikey": os.environ.get("TEQUILA_KEY")
        }
        response = requests.get(url=self.endpoint, params=parameters, headers=header)
        response.raise_for_status()
        flight_date = response.json()['data'][0]['local_departure'].split('T')[0].split('-')
        search_result = {
            "date": f"{flight_date[2]}/{flight_date[1]}/{flight_date[0]}",
            "price": response.json()['data'][0]['price']
        }
#        pprint(search_result)
        return search_result
