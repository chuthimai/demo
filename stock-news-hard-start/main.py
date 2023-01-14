import requests
import datetime
from twilio.rest import Client

account_sid = "ID"
auth_token = "TOKEN"
client = Client(account_sid, auth_token)

today = datetime.date.today()
yesterday = today - datetime.timedelta(days=1)
the_day_before_yesterday = yesterday - datetime.timedelta(days=1)

yesterday = str(yesterday)
the_day_before_yesterday = str(the_day_before_yesterday)

STOCK = "BTCUSDT"
COMPANY_NAME = "bitcoin inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

API_KEY_STOCK = "API"
API_KEY_NEWS = "API"

parameter_stock = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK,
    "datatype": "json",
    "apikey": API_KEY_STOCK,
}

parameter_new = {
    "q": COMPANY_NAME,
    "Date published": "today",
    "Language": "en",
    "apiKey": API_KEY_NEWS,
}

data_stock = requests.get(url=STOCK_ENDPOINT, params=parameter_stock).json()["Time Series (Daily)"]

data_news = requests.get(url=NEWS_ENDPOINT, params=parameter_new).json()["articles"]

data_stock_closing_price = []
some_news = []

data_stock_closing_price.append(data_stock[yesterday]["4. close"])
data_stock_closing_price.append(data_stock[the_day_before_yesterday]["4. close"])

for i in range(3):
    some_news.append({"title": data_news[i]["title"], "url": data_news[i]["url"]})


delta = float(data_stock_closing_price[0]) - float(data_stock_closing_price[1])
percent = delta/float(data_stock_closing_price[1])*100
print(percent)

if percent >= 2 or percent <= -5:
    if percent >= 2:
        message = client.messages.create(
            body=f"BTCUSDT 🔺{round(percent, 2)}%\n\n\n{some_news[0]}\n\n{some_news[1]}\n\n{some_news[2]}",
            from_="number",
            to="number"
        )
    else:
        message = client.messages.create(
            body=f"BTCUSDT 🔻{round(abs(percent), 2)}%\n{some_news[0]}\n{some_news[1]}\n{some_news[2]}",
            from_="number",
            to="number"
        )

