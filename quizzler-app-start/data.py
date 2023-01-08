import requests

parameters = {
    "amount": 30,
    "category": 18,
    "type": "boolean",
}

question_data = requests.get(url="https://opentdb.com/api.php", params=parameters)
question_data = question_data.json()["results"]


