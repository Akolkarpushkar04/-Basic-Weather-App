import requests

# Function to get weather data
def get_weather(city):
    api_key = "your_api_key_here"  # Replace with your OpenWeatherMap API `key`
    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    # Construct final url
    complete_url = f"{base_url}q={city}&appid={api_key}&units=metric"

    # Make the request
    response = requests.get(complete_url)

    # Parse JSON response
    data = response.json()

    if data["cod"] != "404":
        main = data["main"]
        weather = data["weather"][0]

        # Extract and display the information
        temperature = main["temp"]
        humidity = main["humidity"]
        description = weather["description"]

        print(f"City: {city}")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Weather Description: {description.capitalize()}")
    else:
        print("City Not Found!")

if __name__ == "__main__":
    city = input("Enter city name or ZIP code: ")
    get_weather(city)
