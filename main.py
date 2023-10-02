from apikeys import NutrixAppID, NutrixKey
import requests

# Personal data for query
GENDER = "male"
WEIGHT_KG = 88
HEIGHT_CM = 183
AGE = 38

# endpoint for api call to Nutrinionix
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

# get text from user
TEXT = input("What exercise did you just complete? ")

# Header for Nutrix validation
headers = {
    "x-app-id": NutrixAppID,
    "x-app-key": NutrixKey,
    "x-remote-user_id": "0"
}

# Parameters
parameters = {
    "query": TEXT,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

# Nutritionix api call
response = requests.post(exercise_endpoint, json=parameters, headers=headers)
print(response.json())