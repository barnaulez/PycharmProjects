##################### Extra Hard Starting Project ######################
import random

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

####################Solution##############################
# 1. Read birthdays.csv, find all birthdays where day = today, month = current. Make a list of names and mails
# 2. Make a loop

import pandas
import datetime as dt
import os
import smtplib

MY_EMAIL = "alexuvin6@gmail.com"
PASSWORD = "njtkhiswgostspkb"
DIR = "letter_templates"
month = dt.datetime.now().month
day = dt.datetime.now().day


def get_birthdays():
    data = pandas.read_csv("birthdays.csv")
    month_birthdays = data[data.month == month]
    today_birthdays = month_birthdays[month_birthdays.day == day]
    birthdays = today_birthdays.to_dict(orient="records")
    for bday in birthdays:
        filename = DIR + "/" + random.choice(os.listdir(DIR))
        with open(filename) as f:
            template = f.read()
            message = template.replace("[NAME]", bday['name'])
            print(message)
            with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
                connection.starttls()
                connection.login(user=MY_EMAIL, password=PASSWORD)
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=bday['email'],
                    msg=f"Subject:Happy Birthday, {bday['name']}!\n\n{message}")


get_birthdays()