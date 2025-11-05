import requests
import json
import argparse
import sys


API_KEY = "6ea4096301ce8e9ab59d58964a4584d7"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"




def get_weather(city_name):
    
    params = {
        "q": city_name,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(BASE_URL, params=params, timeout=5)

        if response.status_code == 200:
            return json.loads(response.text)
        else:
            print(f"Error: API returned status code {response.status_code}")
            return None

    except requests.exceptions.RequestException as e:
        print(f"Error connecting to weather service: {e}")
        return None


def display_weather(weather_data, city_name):
    
    if weather_data is None:
        print(f"Sorry, could not get weather data for '{city_name}'.")
        return None
    
    
    else:
        
        try:
            
            city = weather_data['name']
            description = weather_data['weather'][0]['description']
            temp = weather_data['main']['temp']
            feels_like = weather_data['main']['feels_like']
            humidity = weather_data['main']['humidity']

            
            print("\n--- Weather Report ---")
            print(f"Location:   {city}")
            print(f"Condition:  {description.title()}")
            print(f"Temp:       {temp}°C")
            print(f"Feels Like: {feels_like}°C")
            print(f"Humidity:   {humidity}%")
            print("----------------------\n")
        
        except KeyError:
            
            print("Error: Could not parse weather data. Response may be incomplete.")



def main():
    
    
    parser = argparse.ArgumentParser(description="Get the current weather for a city.")
    
    
    parser.add_argument("city", nargs="+", help="The name of the city to get weather for.")

    
    args = parser.parse_args()

    
    city_name = " ".join(args.city)

    
    weather_data = get_weather(city_name)
    display_weather(weather_data, city_name)


if __name__ == "__main__":
    main()