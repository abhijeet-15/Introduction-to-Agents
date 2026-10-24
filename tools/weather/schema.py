from .api import get_weather_by_city

weather_tool_schema = {
    "type": "function",
    "function": {
        "name": "get_weather_by_city",
        "description": "Get the current weather and wind speed for a city",
        "parameters": {
            "type": "object",
            "properties": {
                "city_name": {
                    "type": "string",
                    "description": "The name of the city, e.g. London, Tokoyo"
                }
            },
            "required":["city_name"]
        }
    }
}