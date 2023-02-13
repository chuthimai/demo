class FlightData:
    def __init__(self, price, origin_city, origin_airport, destination_city, destination_cityCode, destination_airport, local_departure, local_arrival):
        self.price = price
        self.origin_city = origin_city
        self.origin_airport = origin_airport
        self.destination_city = destination_city
        self.destination_cityCode = destination_cityCode
        self.destination_airport = destination_airport
        self.local_departure = local_departure
        self.local_arrival = local_arrival
        self.stop_over = 0
        self.via_city = []

