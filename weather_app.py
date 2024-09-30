import requests
import coloroma
def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'  # For temperature in Celsius. Use 'imperial' for Fahrenheit.
    }
    response = requests.get(base_url, params=params)
    return response.json()

def display_weather(weather_data):
    if weather_data.get("cod") != 200:
        print("Message", weather_data.get("message"))
        return
    
    city = weather_data['name']
    temp = weather_data['main']['temp']
    description = weather_data['weather'][0]['description']
    
    print(f"Weather in {city}:")
    print(f"Temperature: {temp}°C")
    print(f"Description: {description.capitalize()}")

def main():
    api_key = 'API_KEY' # Replace with your OpenWeatherMap API key
    city = input("Enter city name: ")
    weather_data = get_weather(api_key, city)
    display_weather(weather_data)

if __name__ == "__main__":
    main()
