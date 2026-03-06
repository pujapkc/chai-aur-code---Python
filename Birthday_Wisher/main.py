import smtplib

import datetime as dt
import random

my_email = "choursiyapuja21@gmail.com"
password = "bsghopibebhecave"

now = dt.datetime.now()
weekday = now.weekday()

if weekday ==0:
    with open("./Birthday_Wisher/quotes.txt") as quotefile:
        allquote  = quotefile.readlines()
        quote = random.choice(allquote)


connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=my_email,password=password)
connection.sendmail(
    from_addr=my_email,
    to_addrs="pawan.dandale023@gmail.com",
    msg=f"Subject:Motivation Quote from Puja\n\n {quote}",
)
connection.close()
