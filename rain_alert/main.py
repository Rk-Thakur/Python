import requests # type: ignore

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "f3bf2a000a1b2dbb096b634bd8707a9e"


weather_params = {
    'lat':32.318230,
    'lon':-86.902298,
    'appid':api_key
}
response = requests.get(OWM_Endpoint,params = weather_params)
print(response.status_code)
print(response.json())