##################### Extra Hard Starting Project ######################

import pandas as pd
import smtplib as smtp
import datetime as dt
import random as rd

# 1. Update the birthdays.csv
now = dt.datetime.now()
month = now.month
day = now.day
today = (month, day)

data = pd.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

# 2. Check if today matches a birthday in the birthdays.csv
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
if today in birthdays_dict:
    file_path = f"letter_templates/letter_{rd.randint(1,3)}.txt"
    with open(file_path, "r") as letter:
        birthdays_person = birthdays_dict[today]
        letter = letter.read()
        letter = letter.replace("[NAME]", birthdays_person["name"])

# 4. Send the letter generated in step 3 to that person's email address.
#TODO: delete email and pass before commit
my_email = "email"
my_pass = "pass"
connection = smtp.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=my_email, password=my_pass)
connection.sendmail(
    from_addr=my_email,
    to_addrs=birthdays_person["email"],
    msg=f"Subject:Happy birthday\n\n{letter}"
)
connection.close()




