import requests
from twilio.rest import Client
import os

OWA_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = os.environ.get("OWA_API_KEY")
auth_token = os.environ.get("AUTH_TOKEN")
account_sid = os.environ.get("ACCOUNT_SID")
parameters = {'lat': your_latitude, "lon": your_longitude, "appid": api_key, "exclude": "current,minutely,daily"}
response = requests.get(OWA_Endpoint, params=parameters)
response.raise_for_status()
weather_data = response.json()
hourly_data = weather_data["hourly"]
will_rain = False

for data in hourly_data:
    for data2 in data["weather"]:
        if data2["id"] < 700:
            will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an umbrella ☂️!",
        from_="twillo_phone_number",
        to='phone'
    )
    print(message.status)
