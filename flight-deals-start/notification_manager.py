from twilio.rest import Client
import os


class NotificationManager:
    def __init__(self):
        self.account_id = os.environ.get("ACCOUNT_ID")
        self.auth_token = os.environ.get("AUTH_TOKEN")
        self.client = Client(self.account_id, self.auth_token)

    def send_mess(self, information):
        message = self.client.messages.create(
            body=f"Flight information"
                 f"\n{information.destination_city}: {information.price} VND"
                 f"\nLocal departure: {information.local_departure}"
                 f"\nLocal arrival: {information.local_arrival}",
            from_="+12528887392",
            to="+84987169250"
        )

