import requests


def greet():
    return "Hello Helsinki! 💖"


def get_weather():
    # Helsinki coordinates
    lat, lon = 60.1699, 24.9384
    url = (
        f"https://api.open-meteo.com/v1/forecast?"
        f"latitude={lat}&longitude={lon}&current_weather=true"
    )

    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
        weather = data["current_weather"]
        temp = weather["temperature"]
        wind = weather["windspeed"]
        return f"Current weather: {temp}°C, Wind: {wind} km/h"
    except Exception as e:
        return f"Could not fetch weather: {e}"


def main():
    print(greet())
    print(get_weather())


if __name__ == "__main__":
    main()
