# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 12:40:22 2023

@author: Mosco
"""

import requests

# Replace "your_api_key" with the API key obtained from OpenWeatherMap
API_KEY = "your_api_key"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def get_weather_data(city_name):
    """
    Fetches weather data for the specified city using OpenWeatherMap API.

    :param city_name: The name of the city to fetch weather data for.
    :return: The JSON response containing the weather data.
    """
    params = {
        'q': city_name,
        'appid': API_KEY,
        'units': 'metric',
    }
    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None


def display_weather_data(data):
    """
    Displays the weather data in a readable format.

    :param data: The JSON response containing the weather data.
    """
    if data is None:
        print("Failed to fetch weather data.")
        return

    try:
        city = data['name']
        country = data['sys']['country']
        temp = data['main']['temp']
        weather_desc = data['weather'][0]['description']

        print(f"Weather in {city}, {country}:")
        print(f"{temp}°C, {weather_desc}")
    except KeyError:
        print("Error: Could not parse weather data.")


if __name__ == "__main__":
    city_name = input("Enter the city name: ")
    weather_data = get_weather_data(city_name)
    display_weather_data(weather_data)
