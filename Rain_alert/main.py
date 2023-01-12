import requests
from twilio.rest import Client

account_sid = "ID"
auth_token = "AUTH_TOKEN"
api_key = "API_KEY"
# location: Hai Duong, Vietnam
parameters = {
    "lat": 20.937342,
    "lon": 106.314552,
    "appid": api_key,
}

response = requests.get(
    url="https://api.openweathermap.org/data/2.5/forecast",
    params=parameters,
)

data = response.json()["list"]
weather_data = []
for i in range(4):
    weather_data.append(data[i]['weather'][0]['id'])
print(weather_data)

will_rain = False
for i in range(4):
    if weather_data[i] < 700:
        will_rain = True
        break
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an umbrella ☔️☔☔",
        from_="number",
        to="number"
    )
    print(message.status)








