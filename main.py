from apikeys import NutrixAppID, NutrixKey, SheetyToken
import requests

# Personal data for query
GENDER = "male"
WEIGHT_KG = 88
HEIGHT_CM = 183
AGE = 38

# endpoint for api call to Nutrinionix and Sheety
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = "https://api.sheety.co/afb11dba9362fa1a06c43e30af90187c/myWorkouts/workouts"

# get text from user
TEXT = input("What exercise did you just complete? ")

# Header for Nutrix validation
headers_nutrix = {
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
response = requests.post(exercise_endpoint, json=parameters, headers=headers_nutrix)
data = response.json()
print(data["exercises"][0])

print(data["exercises"][0]['duration_min'])
print(f"the type of exercise: {data['exercises'][0]['name']} number of calories burned {data['exercises'][0]['nf_calories']}, and the time spend {data['exercises'][0]['name']}: {data['exercises'][0]['duration_min']}")



headers_sheety = {
    "Authorization": SheetyToken
}

# response = requests.post(sheety_endpoint, json=parameters, headers=headers_sheety)