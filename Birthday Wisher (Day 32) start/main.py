import smtplib as smtp
import datetime as dt
import random as rd

now = dt.datetime.now()
weekday = now.weekday()

if weekday == 2:
    with open("quotes.txt", "r") as data:
        all_quotes = data.readlines()
        quote = rd.choice(all_quotes)

#TODO: delete email and pass before commit
my_email = "email"
my_pass = "pass"
my_other_email = "email"

connection = smtp.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=my_email, password=my_pass)
connection.sendmail(from_addr=my_email,
                    to_addrs=my_other_email,
                    msg=f"Subject:Greeting\n\n{quote}")
connection.close()



