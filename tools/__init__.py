from .weather.schema import weather_tool_schema
from .weather.api import get_weather_by_city

#registry
AVAILABLE_TOOLS = {
    "get_weather_by_city": get_weather_by_city,
}

TOOL_SCHEMAS = [weather_tool_schema]