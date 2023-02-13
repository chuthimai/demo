import requests
from flight_data import FlightData
import os


class FlightSearch:
    def __init__(self):
        self.endpoint_tequila = "https://tequila-api.kiwi.com"
        self.API_KEY = os.environ.get("API_KEY")

    def get_code(self, city_name):
        header = {"apikey": self.API_KEY}
        query = {
            "term": city_name,
            "location_types": "city",
        }

        response = requests.get(
            url=f"{self.endpoint_tequila}/locations/query",
            headers=header,
            params=query
        ).json()["locations"]
        code = response[0]["code"]
        return code

    def check_flight(self, from_city, to_city, date_from, date_to):
        header = {"apikey": self.API_KEY}
        query = {
            "fly_from": self.get_code(from_city),
            "fly_to": self.get_code(to_city),
            "date_from": date_from.strftime("%d/%m/%Y"),
            "date_to": date_to.strftime("%d/%m/%Y"),
            "one_for_city": 1,
            "one_per_date": 1,
            "adults": 1,
            "curr": "VND",
            "max_stopovers": 2,
        }

        response = requests.get(url=f"{self.endpoint_tequila}/v2/search", headers=header, params=query)

        try:
            data = response.json()["data"][0]
            flight_way = response.json()["data"][0]["route"]
        except IndexError:
            print(f"No flights found for {to_city}.")
            return None
        city_through = [from_city]
        for inf in flight_way:
            city_through.append(inf['cityTo'])

        data_flight = FlightData(
            price=round(int(data["price"]), -3),
            origin_city=from_city,
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=to_city,
            destination_cityCode=self.get_code(to_city),
            destination_airport=data["route"][0]["flyTo"],
            local_departure=data["route"][0]["local_departure"].split("T")[0],
            local_arrival=data["route"][0]["local_arrival"].split("T")[0],
        )
        data_flight.stop_over = len(flight_way) - 1
        data_flight.via_city = city_through

        print(f"Price: {data_flight.price} VND")
        print(f"Local departure: {data_flight.local_departure}")
        print(f"City through: {data_flight.via_city}")
        return data_flight


