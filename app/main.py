import time
import requests
import sys

def greet():
    return "Hello Helsinki! 💖"

def pause():
    return "Wait a bit "

def loading_bar():
    total_time = 60  # Duration of the loading in seconds
    total_steps = total_time  # Total number of "+" characters to print (1 per second)
    
    sys.stdout.write("Loading: ")
    sys.stdout.flush()

    for i in range(total_steps + 1):  # We want to print `total_steps` "+" symbols
        progress = "█" * i  # String of "+" symbols, based on the current step
        percentage = (i * 100) // total_steps  # Calculate the percentage
        sys.stdout.write(f"\rLoading: {progress: <{total_steps}} %{percentage:3}")
        sys.stdout.flush()
        time.sleep(1)  # Wait for 1 second before the next step

    sys.stdout.write("\n")  # Move to the next line after the loading completes

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
        return f"Current weather: {temp}°C 🌡️ \nWind: {wind} km/h 🌬️"
    except Exception as e:
        return f"Could not fetch weather: {e}"


def main():
    print(greet())
    while True:
        print(get_weather())
        loading_bar()  # Wait for 1 minute


if __name__ == "__main__":
    main()
