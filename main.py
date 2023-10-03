from apikeys import NutrixAppID, NutrixKey, SheetyToken, Google_Sheet_Endpoint
import requests
from datetime import datetime

# Personal data for query
GENDER = "male"
WEIGHT_KG = 88
HEIGHT_CM = 183
AGE = 38

# endpoint for api call to Nutrinionix and Sheety
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = Google_Sheet_Endpoint
GOOGLE_SHEET_NAME = "sheet1"

# get text from user
TEXT = input("What exercise did you just complete? ")

# Header for Nutrix validation
headers_nutrix = {
    "x-app-id": NutrixAppID,
    "x-app-key": NutrixKey,
    "x-remote-user_id": "0"
}

# Parameters
nutritionix_parameters = {
    "query": TEXT,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

# Nutritionix api call
response = requests.post(exercise_endpoint, json=nutritionix_parameters, headers=headers_nutrix)
data = response.json()

# import the date and time
today_date = datetime.now().strftime("%m/%d/%Y")
current_time = datetime.now().strftime("%X")

headers_sheety = {
    "Authorization": f"Bearer {SheetyToken}"
}

for exercise in data["exercises"]:
    print(exercise['duration_min'])
    sheety_parameters = {
        GOOGLE_SHEET_NAME: {
            "date": today_date,
            "time": current_time,
            "exercise": exercise["name"],
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }

    }
    response = requests.post(sheety_endpoint, json=sheety_parameters, headers=headers_sheety)
    print(response.text)
