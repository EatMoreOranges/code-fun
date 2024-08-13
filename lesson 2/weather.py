# Import the requests library
import requests

# Define a class named Weather
class Weather:
    # The __init__ method initializes the object's attributes
    def __init__(self, city, api_key):
        self.city = city  # Instance variable for the city name
        self.api_key = api_key  # Instance variable for the API key
        self.api_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

    # Method to get weather information from the OpenWeatherMap API
    def get_weather_info(self):
        response = requests.get(self.api_url)  # Make a GET request to the API
        return response.json()  # Return the JSON response

    # Method to get the current temperature
    def get_temperature(self):
        weather_info = self.get_weather_info()
        temp_kelvin = weather_info['main']['temp']
        temp_celsius = temp_kelvin - 273.15  # Convert from Kelvin to Celsius
        return temp_celsius

    # Method to get the current humidity
    def get_humidity(self):
        weather_info = self.get_weather_info()
        return weather_info['main']['humidity']

# Example usage
api_key = "your_openweathermap_api_key"  # Replace with your OpenWeatherMap API key
weather = Weather("London", api_key)

# Get and print the current temperature and humidity
print(f"Temperature: {weather.get_temperature()}°C")
print(f"Humidity: {weather.get_humidity()}%")