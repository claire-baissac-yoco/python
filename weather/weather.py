import requests
from const import API_URL, API_KEY


def fetch_weather_data(city: str) -> str:
    payload = {'key': API_KEY, 'q': city, 'aqi': "no"}
    response = requests.get(API_URL, params=payload)
    data = response.json()
    current_temp = data['current']['temp_c']
    return current_temp


if __name__ == "__main__":
    data = fetch_weather_data("Cape Town")
    print(data)
