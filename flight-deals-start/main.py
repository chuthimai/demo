from data_manager import DataManager
import datetime


today = datetime.date.today()
after_60days = today + datetime.timedelta(days=60)

from_city = "Ha Noi"
to_city = input(f"Search the flight from {from_city} to ")

data = DataManager(from_city=from_city, to_city=to_city, date_from=today, date_to=after_60days)
data.put_lowest_prices()




















