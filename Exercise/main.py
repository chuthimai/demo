import requests
import datetime as dt
import os

account_id = os.environ.get("ACCOUNT_ID")
API_KEY = os.environ.get("API_KEY")
endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
TOKEN = os.environ.get("TOKEN")

headers = {
    "x-app-id": account_id,
    "x-app-key": API_KEY
}

sentence = input("Tell me which exercises you did: ")

params = {
 "query": sentence,
 "gender": "female",
 "weight_kg": 49.0,
 "height_cm": 145.0,
 "age": 20
}

response = requests.post(url=endpoint, headers=headers, json=params)
response = response.json()
response = response["exercises"]


def post_exercise(exercise, duration, calories):
    now = dt.datetime.now()
    time = now.strftime("%H:%M:%S")
    date = now.strftime("%d/%m/%Y")

    endpoint_sheet = os.environ.get("ENDPOINT_SHEET")
    headers_sheet = {
        "authorization": TOKEN
    }
    params_sheet = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": exercise.title(),
            "duration": duration,
            "calories": calories,
        }
    }

    requests.post(url=endpoint_sheet, headers=headers_sheet, json=params_sheet)


for i in response:
    exercise = i["name"]
    duration = i["duration_min"]
    calories = i["nf_calories"]
    post_exercise(exercise, duration, calories)















