#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import os
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
from pprint import pprint
from datetime import datetime
from datetime import timedelta

data_mng = DataManager()
nm = NotificationManager()

search = FlightSearch(data_mng.get_iata(os.environ.get("CITY_FROM")))


flight_list = []
sheet_data = data_mng.get_flights()

for row in sheet_data:
    if row["iataCode"] == '':
        row["iataCode"] = data_mng.get_iata(row["city"])
data_mng.update_flights(sheet_data)
today = datetime.now()
tomorrow = today + timedelta(days=1)
end_date = today + timedelta(days=90)

for row in sheet_data:
    result = search.flight_search(tomorrow.strftime("%d/%m/%Y"), end_date.strftime("%d/%m/%Y"), row["iataCode"])
    pprint(row)
    if row["lowestPrice"] > result["price"]:
        row["lowestPrice"] = result["price"]
        row["date"] = result["date"]
        nm.send_notification(row["date"], row["city"], row["lowestPrice"])
data_mng.update_flights(sheet_data)