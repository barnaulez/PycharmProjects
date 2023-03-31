import requests
from datetime import datetime
import time
import smtplib

MY_LAT = 38.423733
MY_LON = 27.142826
MY_EMAIL = "alexuvin6@gmail.com"
PASSWORD = "MY_PASSWORD_HERE"
parameters = {
    "lat": MY_LAT,
    "lng": MY_LON,
    "formatted": 0
}

time_now = datetime.now()

def get_iss_position():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()["iss_position"]
    return data

def get_my_position():
    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()["results"]
    sunrise = int(data["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["sunset"].split("T")[1].split(":")[0])
    times = {
        "sunrise": sunrise,
        "sunset": sunset,
        "current_time": time_now.hour
    }
    return times

def send_mail(coordinates):
    iss_latitude = coordinates["latitude"]
    iss_longitude = coordinates["longitude"]
    message = f"""Hey!\n
    Now you can see ISS!\n
    It's coordinates:\n
    Latitude: {iss_latitude}\n
    Longitude: {iss_longitude}
    """
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="barnaulez@gmail.com",
            msg=f"Subject:ISS is over head!\n\n{message}")

def check_visibility():
    iss_coordinates = get_iss_position()
    print(iss_coordinates)
    lat_delta = MY_LAT - float(iss_coordinates["latitude"])
    lon_delta = MY_LON - float(iss_coordinates["longitude"])
    print(lat_delta, lon_delta)
    if abs(lat_delta) <= 5 and abs(lon_delta) <= 5:
        times = get_my_position()
        if 24 > times["current_time"] > times["sunset"]+3 or 0 < times["current_time"] < times["sunrise"]+3:
            print("You can see!")
            send_mail(iss_coordinates)
    else:
        print("ISS is not visible")
    time.sleep(120)
    check_visibility()

check_visibility()
