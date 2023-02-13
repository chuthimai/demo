from twilio.rest import Client
import os
import smtplib


class NotificationManager:
    def __init__(self):
        self.account_id = os.environ.get("ACCOUNT_ID")
        self.auth_token = os.environ.get("AUTH_TOKEN")
        self.client = Client(self.account_id, self.auth_token)
        self.MY_EMAIL = os.environ.get("MY_EMAIL")
        self.MY_PASSWORD = os.environ.get("MY_PASSWORD")
        self.my_tel = os.environ.get("TEL")

    def send_mess(self, information):
        print(self.account_id)
        print(self.auth_token)
        message = self.client.messages.create(
            body=f"Flight information"
                 f"\n{information.destination_city}: {information.price} VND"
                 f"\nDate: {information.local_departure}"
                 f"\nCity through: {information.via_city}",
            from_="+12528887392",
            to=self.my_tel
        )
        print(message.sid)

    def send_email(self, information):
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(self.MY_EMAIL, self.MY_PASSWORD)
        connection.sendmail(
            from_addr=self.MY_EMAIL,
            to_addrs="chuthimai18245@gmail.com",
            msg=f"Subject:Flight information\n\n"
                f"\nFrom {information.origin_city} to {information.destination_city}: {information.price} VND"
                f"\nDate: {information.local_departure}"
                f"\nCity through: {information.via_city}"
        )

