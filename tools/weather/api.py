import requests

def get_weather_by_city(city_name: str) -> str:
    """ look up the weather for a city """

    geocode_url = "https://geocoding-api.open-meteo.com/v1/search"
    geocode_params = {
        "name": city_name,
        "count": 1
    }

    response = requests.get(geocode_url,params=geocode_params)
    if response.status_code != 200:
        return f"failed to connect to the geocodig service"
    
    data = response.json()

    if "results" not in data:
        return f"City: {city_name} not found."

    location = data["results"][0]
    lat = location["latitude"]
    lon = location["longitude"]
    country = location["country"]

    #print(f" details found: {lat}\t{lon}\t{country}\n")

    weather_url = "https://api.open-meteo.com/v1/forecast"
    weather_params = {
        "latitude": lat,
        "longitude": lon,
        "current": ["temperature_2m", "wind_speed_10m"]
    }

    weather_response = requests.get(weather_url, params=weather_params)
    
    if weather_response.status_code != 200:
        return f"failed to fetch the weather"

    weather_data =  weather_response.json()
    current = weather_data["current"]
    units = weather_data["current_units"]
    return f"temperature is {current["temperature_2m"]}{units["temperature_2m"]} and windspeed is {current["wind_speed_10m"]}{units["wind_speed_10m"]}\n" 


get_weather_by_city("Tatanagar")

