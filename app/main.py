import time
import requests

# API URL for Open-Meteo (Helsinki, Finland)
URL = "https://api.open-meteo.com/v1/forecast"
PARAMS = {
    "latitude": 60.1699,  # Helsinki Latitude
    "longitude": 24.9384,  # Helsinki Longitude
    "current_weather": "true"  # Get the current weather
}

def get_weather():
    try:
        # Request weather data from Open-Meteo API
        response = requests.get(URL, params=PARAMS)
        if response.status_code == 200:
            data = response.json()
            weather = data['current_weather']
            temperature = weather['temperature']
            wind_speed = weather['windspeed']
            weather_condition = weather['weathercode']
            
            # Convert weather condition code to human-readable format
            weather_conditions = {
                0: "Clear sky",
                1: "Partly cloudy",
                2: "Cloudy",
                3: "Overcast",
                45: "Fog",
                48: "Depositing rime fog",
                51: "Light drizzle",
                53: "Moderate drizzle",
                55: "Heavy drizzle",
                56: "Light freezing drizzle",
                57: "Heavy freezing drizzle",
                61: "Light rain",
                63: "Moderate rain",
                65: "Heavy rain",
                66: "Light freezing rain",
                67: "Heavy freezing rain",
                71: "Light snow",
                73: "Moderate snow",
                75: "Heavy snow",
                77: "Snow grains",
                80: "Light showers of rain",
                81: "Moderate showers of rain",
                82: "Heavy showers of rain",
                85: "Light showers of snow",
                86: "Heavy showers of snow",
                95: "Thunderstorms",
                96: "Thunderstorms with light hail",
                99: "Thunderstorms with heavy hail"
            }
            weather_desc = weather_conditions.get(weather_condition, "Unknown weather")
            
            print(f"Weather in Helsinki: {weather_desc}")
            print(f"Temperature: {temperature}°C 🌡️")
            print(f"Wind Speed: {wind_speed} km/h 🌬️")
        else:
            print(f"Failed to get data: {response.status_code}")
    except Exception as e:
        print(f"Error while fetching weather: {e}")

def greet():
    print("Hello Helsinki! 💖")

def main():
    greet()
    while True:
        get_weather()
        time.sleep(60)  # Wait for 1 minute

if __name__ == "__main__":
    main()
