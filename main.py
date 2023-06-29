import math
import requests
import datetime as dt

APP_ID = "YOUR_API_ID"
API_KEY = "YOUR_API_KEY"
ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
gender = "YOUR_GENDER"
weight_kg = "YOUR_WIGHT"
height_cm = "YOUR HEIGHT"
age = "YOUR_AGE"
headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": input("Tell me which exercise you did: "),
    "gender": gender,
    "weight_kg": float(weight_kg),
    "height_cm": float(height_cm),
    "age": int(age)
}

request = requests.post(url=ENDPOINT, headers=headers, json=parameters)
request.raise_for_status()
print(request.json())
workout_data = request.json()
workout_list = workout_data['exercises']

workout_sheet = "https://api.sheety.co/YOUR_SHEETY_API/myWorkouts/workouts"

for list_num in range(len(workout_list)):
    workout_name = workout_list[list_num]['name']
    workout_duration = round(workout_list[list_num]['duration_min'])
    burned_calories = math.floor(workout_list[list_num]['nf_calories'])
    now = dt.datetime.now()
    current_day = now.strftime("%d/%m/%Y")
    current_time = now.strftime("%X")

    hearders = {
        "Authorization": "Bearer YOUR_TOKEN"
    }

    workout_sheet_parameters = {
        "workout": {
            "date": current_day,
            "time": current_time,
            "exercise": workout_name.title(),
            "duration": workout_duration,
            "calories": burned_calories,
        }
    }

    sheety_request = requests.post(url=workout_sheet, json=workout_sheet_parameters, headers=hearders)
    print(sheety_request.text)
