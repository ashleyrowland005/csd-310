import requests

# Test connection
response = requests.get("https://www.google.com")

print("Status Code:", response.status_code)

# ----------------------------
# Weather API Section
# ----------------------------

weather_url = "https://api.open-meteo.com/v1/forecast?latitude=41.25&longitude=-95.93&current_weather=true"

weather_response = requests.get(weather_url)

print("\nWeather API Status Code:", weather_response.status_code)

weather_data = weather_response.json()

print("\n--- Raw Weather Response ---")
print(weather_data)

print("\n--- Formatted Weather Output ---")

current = weather_data["current_weather"]

print("Current Temperature:", current["temperature"], "°C")
print("Wind Speed:", current["windspeed"], "km/h")
print("Weather Code:", current["weathercode"])

