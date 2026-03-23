import os
import requests
import time
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")

if not API_KEY:
    raise ValueError("API_KEY not found in environment variables")

url = f"https://api.openweathermap.org/data/2.5/weather?q=London&appid={API_KEY}"

try:

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        temp = data.get("main", {}).get("temp")
        print("Temperature:", temp)

    elif response.status_code == 401:
        print("Invalid API key. Check your .env file.")

    elif response.status_code == 429:
        print("Rate limit hit. Retrying in 60 seconds...")
        time.sleep(60)

    else:
        print(f"Error: {response.status_code}")
        print(response.text)

except requests.exceptions.Timeout:
            print("Request timed out. Please try again later.")


# print(f"Fetching weather for: {city}...")

# Do NOT log user-provided location data (e.g., city names). 
# Location information can be considered personal data under GDPR.
# Logging such data without consent violates privacy and data minimization principles.