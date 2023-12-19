import requests

def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": api_key}

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        weather_data = response.json()
        return weather_data
    else:
        return None

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def main():
    # Replace 'YOUR_API_KEY' with your actual OpenWeatherMap API key
    api_key = 'YOUR_API_KEY'

    if api_key == 'YOUR_API_KEY':
        print("Please replace 'YOUR_API_KEY' with your actual OpenWeatherMap API key.")
        return

    city = input("Enter the name of the municipality: ")

    weather_data = get_weather(api_key, city)

    if weather_data:
        description = weather_data['weather'][0]['description']
        temperature_kelvin = weather_data['main']['temp']
        temperature_celsius = kelvin_to_celsius(temperature_kelvin)

        print(f"Weather in {city}:")
        print(f"Condition: {description}")
        print(f"Temperature: {temperature_celsius:.2f} °C")
    else:
        print(f"Failed to fetch weather data for {city}. Please check the city name and try again.")

if __name__ == "__main__":
    main()
