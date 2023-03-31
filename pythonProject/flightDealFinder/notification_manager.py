import requests
import os
class NotificationManager:
    def __init__(self):
        self.token = os.environ.get("BOT_TOKEN")
        self.chat = os.environ.get("CHAT_ID")

    def send_notification(self, flight_date, destination, new_price):
        departure = os.environ.get("CITY_FROM")
        message = f"Hey! I've found new lowest price for flight from {departure} to {destination}. New price: €{new_price}. Flight date: {flight_date}. Hurry up to buy tickets!"
        send_text = 'https://api.telegram.org/bot' + self.token + '/sendMessage?chat_id=' + self.chat + '&parse_mode=Markdown&text=' + message
        response = requests.get(send_text)
        print(response.json())