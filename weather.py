import requests

API_KEY = "43164d29ef676e5e18a79292bfb71c4d"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city name: ")
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
# get the temperature, transfor to Celsious and round the float number to 0.0
    temperature = round(data["main"]["temp"]-273.15, 1)
    print(
        f"The temperature in {city.capitalize()} now is: {temperature}ºC with {weather.capitalize()}")
else:
    print("An error occurred.")
