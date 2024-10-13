import requests


def get_weather_info(message: str):
    API_KEY = "3b9f634f9b44edfa0562a0158d5a1d46"

    url = "https://api.openweathermap.org/data/2.5/weather?"
    params = {"appid": API_KEY, "units": "metric", "lang": "en", "q": message}
    data = requests.get(url, params=params).json()

    temp = data["main"]["temp"]
    wind_speed = data["wind"]["speed"]
    desc = data["weather"][0]["description"]
    main = data["weather"][0]["main"]
    emoji = []
    main2 = ["Mist", 'Smoke', 'Haze', 'Dust', 'Fog', 'Sand', 'Ash', 'Squall', 'Tornado']

    if main == "Thunderstorm":
        emoji.append("🌩")
    elif main == "Rain":
        emoji.append("🌧")
    elif main == "Drizzle":
        emoji.append("🌦")
    elif main == "Snow":
        emoji.append("🌨")
    elif main in main2:
        emoji.append("🌫")
    elif main == "Clear":
        emoji.append("☀️")
    elif main == "Clouds":
        emoji.append("☁️")

    return f"""
In the city {message.capitalize()} now {desc} {emoji[0]}
Temperature: {temp}°C
Wind speed: {wind_speed}m/s
"""


# get_weather_info("tashkent")
