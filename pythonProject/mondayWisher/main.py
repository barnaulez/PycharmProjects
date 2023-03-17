import datetime as dt
import random
import smtplib

my_email = "alexuvin6@gmail.com"
password = "njtkhiswgostspkb"

now = dt.datetime.now()
if now.weekday() == 3:
    try:
        f = open("quotes.txt", mode="r")
    except FileNotFoundError:
        print("Wishes base not found")
    else:
        wish = random.choice(f.readlines())
        f.close()
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs="barnaulez@gmail.com",
                msg=f"Subject:Hello!\n\n{wish}")
