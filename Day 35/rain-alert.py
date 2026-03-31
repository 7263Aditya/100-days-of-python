import requests
import os
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast?"
api_key = "62e88476152e510b52c6196356d7ecf6"
account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
auth_token = os.environ.get('TWILIO_AUTH_TOKEN')


weather_params = {
    "lat": -22.932924,
    "lon": -47.073845,
    "appid": api_key,
    "cnt":4,
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
# print(weather_data["list"][0]["weather"][0]["id"])
will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) <700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    def send_alert(message_body):
        message = client.messages.create(
            from_='whatsapp:+14155238886',
            body="It's going to rain today! 🌧️ Take an umbrella.",
            to='whatsapp:+917263970149'
        )
        print("It's going to rain today! 🌧️ Take an umbrella.")
    send_alert("It's going to rain today!")