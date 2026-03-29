import requests
from datetime import datetime

# response = requests.get(url="https://api.open-notify.org/iss-now.json")
# response.raise_for_status()
#
# data = response.json()
# # print(data)
#
# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]
# iss_position = (longitude, latitude)
# print(iss_position)

my_lat = 18.732997
my_lang = 73.678840

parameters = {
    'lat':my_lat,
    'lng':my_lang,
    'formatted': 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data['results']['sunrise'].split('T')[1].split(':')[0]
sunset = data['results']['sunset'].split('T')[1].split(':')[0]
print(sunrise)
print(sunset)
time_now = datetime.now()
print(time_now)
print(sunset)