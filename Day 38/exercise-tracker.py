import requests
from datetime import datetime

APP_ID = "app_8c825c9bf009436da5c0efc"
API_KEY = "nix_live_8U7kjDMjBwCmaFWMTSexXYbaLdYp8T1"
SHEET_ENDPOINT = "https://api.sheety.co/d22384f0b7a7bd93ac99e00c6b18680a/myWorkout/sheet1"

USERNAME = "Aditya"
PASSWORD = "Adi$"

exercise_endpoint = "https://app.100daysofpython.dev/v1/nutrition/natural/exercise"

exercise_text = input("Tell me which exercises you did?: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}
user_params = {
    "query": exercise_text,
    "gender": "male",
    "weight_kg": 103,
    "height_cm": 168,
    "age": 25,
}

response = requests.post(url=exercise_endpoint, json=user_params, headers=headers)
result = response.json()

if "exercises" not in result:
    print("❌ Nutritionix Error. Check your App ID and API Key:")
    print(result)
else:
    print("✅ Success! Data received. Sending to Sheety...")

    today_date = datetime.now().strftime("%d/%m/%Y")
    now_time = datetime.now().strftime("%X")

    for exercise in result["exercises"]:
        sheet_inputs = {
            "sheet1": {
                "date": today_date,
                "time": now_time,
                "exercise": exercise["name"].title(),
                "duration": exercise["duration_min"],
                "calories": exercise["nf_calories"]
            }
        }
        sheet_response = requests.post(url=SHEET_ENDPOINT, json=sheet_inputs,auth=(USERNAME,PASSWORD))
        print(f"Sheety Status: {sheet_response.status_code} - {sheet_response.text}")