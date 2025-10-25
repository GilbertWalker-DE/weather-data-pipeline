import requests
api_key = "01859f3bd712dce412941593ae605042"
api_url = f"http://api.weatherstack.com/current?access_key={api_key}&query=New York"

def fetch_data():
    print("Fetching weather data from Weatherstack API...")
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        print("API response received succcessfully.")
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        raise


def mock_fetch_data():
    return {'request': {'type': 'City', 'query': 'New York, United States of America', 'language': 'en', 'unit': 'm'}, 'location': {'name': 'New York', 'country': 'United States of America', 'region': 'New York', 'lat': '40.714', 'lon': '-74.006', 'timezone_id': 'America/New_York', 'localtime': '2025-10-21 20:05', 'localtime_epoch': 1761077100, 'utc_offset': '-4.0'}, 'current': {'observation_time': '12:05 AM', 'temperature': 17, 'weather_code': 113, 'weather_icons': ['https://cdn.worldweatheronline.com/images/wsymbols01_png_64/wsymbol_0008_clear_sky_night.png'], 'weather_descriptions': ['Clear '], 'astro': {'sunrise': '07:14 AM', 'sunset': '06:06 PM', 'moonrise': '07:24 AM', 'moonset': '05:54 PM', 'moon_phase': 'New Moon', 'moon_illumination': 0}, 'air_quality': {'co': '176.85', 'no2': '20.55', 'o3': '77', 'so2': '5.75', 'pm2_5': '8.35', 'pm10': '8.95', 'us-epa-index': '1', 'gb-defra-index': '1'}, 'wind_speed': 21, 'wind_degree': 182, 'wind_dir': 'S', 'pressure': 1010, 'precip': 0, 'humidity': 65, 'cloudcover': 0, 'feelslike': 17, 'uv_index': 0, 'visibility': 16, 'is_day': 'no'}}

