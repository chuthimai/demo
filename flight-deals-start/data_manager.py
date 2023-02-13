import requests
from flight_search import FlightSearch
from notification_manager import NotificationManager
import os


class DataManager(FlightSearch):
    def __init__(self, from_city, to_city, date_from, date_to):
        super().__init__()
        self.endpoint_sheet = os.environ.get("ENDPOINT_SHEET")
        self.data_sheet = requests.get(url=self.endpoint_sheet).json()["prices"]
        self.from_city = from_city
        self.to_city = to_city
        self.date_from = date_from
        self.date_to = date_to

    def put_lowest_prices(self):
        flight = self.check_flight(self.from_city, self.to_city, self.date_from, self.date_to)
        destination_city_code = flight.destination_cityCode
        city_has_gone = False

        for i in self.data_sheet:
            if destination_city_code == i['iataCode']:
                city_has_gone = True
                if flight.price <= i['lowestPrice']:
                    endpoint_put = f"{self.endpoint_sheet}/{i['id']}"
                    parameter_sheet = {
                        "price": {
                            "lowestPrice": flight.price,
                        }
                    }
                    requests.put(url=endpoint_put, json=parameter_sheet)
                break

        if not city_has_gone:
            parameter_sheet = {
                "price": {
                    "city": flight.destination_city,
                    "iataCode": flight.destination_cityCode,
                    "lowestPrice": flight.price,
                }
            }
            requests.post(url=self.endpoint_sheet, json=parameter_sheet)
            city_has_gone = True

        if city_has_gone:
            notification = NotificationManager()
            notification.send_email(flight)









