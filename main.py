import requests
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

account_sid = 'YOUR TWILIO ACCOUNT_SID'
auth_token = 'YOUR TWILIO AUTH_TOKEN'

parameters = {
    "lat": "YOU LATITUDE",
    "lon": "YOUR LONGITUDE",
    "appid": "YOUR APPID",
    "exclude": "current,minutely,daily"
}

api = requests.get(url="your open_weather API", params=parameters)
data = api.json()

will_rain = False
hour_slice = data["hourly"][:12]
fore_cast_weather_code_12_hour = [cond_code["weather"][0]["id"] for cond_code in hour_slice]

print(data["hourly"][:12])

for code in fore_cast_weather_code_12_hour:
    if int(code) < 700:
        will_rain = True
if will_rain:
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}
    client = Client(account_sid, auth_token, http_client=proxy_client)
    message = client.messages.create(
        from_='whatsapp:YOUR TWILIO NUMBER',
        body='YOUR MASSAGE',
        to='whatsapp:NUMBER TO SEND'
    )





