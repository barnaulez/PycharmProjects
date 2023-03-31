import requests
from twilio.rest import Client

api_key = "API"

account_sid = "SID"
auth_token = "TOKEN"
MY_LAT = 38.454799
MY_LON = 27.115196



parameters = {
    "lat": MY_LAT,
    "lon": MY_LON,
    "exclude": "current,minutely,daily",
    "appid": api_key
}

will_rain = False

def get_weather():
    response = requests.get(url="https://api.openweathermap.org/data/3.0/onecall", params=parameters)
    response.raise_for_status()
    print(response.status_code)
    weather_data = response.json()["hourly"][:12]
    for weather in weather_data:
        if weather["weather"][0]['id'] < 700:
            will_rain = True
            break

def send_sms():
    get_weather()
    client = Client(account_sid, auth_token)
    if will_rain:
        message = client.messages.create(to="+15076232492", body="Bring an Umbrella", from_="+15076232492")
        print(message.status)
    else:
        message = client.messages.create(to="+15076232492", body="You don't need an Umbrella today", from_="+15076232492")
        print(message.status)

def send_telegram_message():
    get_weather()
    bot_message = ""
    bot_token = 'BOT_TOKEN'
    bot_chatID = '172133786'
    if will_rain:
        bot_message = "Bring an Umbrella"
    else:
        bot_message = "You don't need an Umbrella today"
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)
    print(response.json())

send_telegram_message()
