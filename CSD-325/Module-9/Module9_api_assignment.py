import requests

# Test connection
response = requests.get("https://www.google.com")

print("Status Code:", response.status_code)

# ----------------------------
# Astronaut API Section
# ----------------------------

astro_url = "http://api.open-notify.org/astros.json"

astro_response = requests.get(astro_url)

print("\nAstronaut API Status Code:", astro_response.status_code)

astro_data = astro_response.json()

print("\n--- Raw Astronaut Response ---")
print(astro_data)

print("\n--- Formatted Astronaut Output ---")
print("There are", astro_data["number"], "astronauts in space:\n")

for person in astro_data["people"]:
    print(person["name"], "is on", person["craft"])
