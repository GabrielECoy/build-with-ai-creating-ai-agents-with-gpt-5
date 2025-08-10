"""
Build with AI: Creating AI Agents with GPT-5
All examples use Python and the OpenAI client.

Prereqs:
  pip install openai
  pip install python-dotenv
  export API_KEY = os.environ[...]
"""
import os
from openai import OpenAI
from dotenv import load_dotenv, find_dotenv
from agents import Agent, Runner, function_tool
from dataclasses import dataclass
from datetime import datetime
import requests

# read local .env file
_ = load_dotenv(find_dotenv()) 

# retrieve OpenAI API key
client = OpenAI(
  api_key=os.environ['OPENAI_API_KEY']  
)

# # ---------------------------------------------------------------------------
# # LESSON 2 (Build a Basic Agent with Tool Calling)
# # ---------------------------------------------------------------------------
@dataclass
class WeatherInfo:
    city: str
    country: str
    temp_f: float
    condition: str

@function_tool
def get_weather_forecast(city: str):
    """Fetch weather info using the Weather API - https://www.weatherapi.com/
       Create an account and generate your API key - https://www.weatherapi.com/my/ 
    """
    API_KEY = api_key=os.environ['WEATHER_API_KEY']
    WEATHER_BASE_URL = 'https://api.weatherapi.com/v1/current.json'

    try:
        today = datetime.today().strftime('%Y-%m-%d')
        params = {"q": city, "aqi": "no", "key": API_KEY}
        
        #construct request and call api
        response = requests.get(WEATHER_BASE_URL, params=params)
        response.raise_for_status()

        data = response.json()

        # Basic validation
        if "location" not in data or "current" not in data:
            return f"Could not retrieve weather for '{city}'. Try a more specific place name."

        weather = WeatherInfo(
            city=data["location"]["name"],
            country=data["location"]["country"],
            temp_f=float(data["current"]["temp_f"]),
            condition=data["current"]["condition"]["text"]
        )

        weather_report = [f"Real-time weather report for {today}:"]

        weather_report.append(
                f"   - City: {weather.city}"
                f"   - Country: {weather.country}"
                f"   - Temperature: {weather.temp_f:.1f} °F"
                f"   - Weather Conditions: {weather.condition}"
            )

        return "\n".join(weather_report)
    except requests.exceptions.RequestException as e:
        return f"Error fetching weather data: {str(e)}"

trip_agent = Agent(
    name="Trip Coach",
    instructions=(
        "You help travelers plan by checking real-time weather."
        "When asked about weather or packing, CALL the get_weather_forecast tool."
        "Make sure you have access to real-time weather data to make your recommendations."
    ),
    model="gpt-5",
    tools=[get_weather_forecast]
)

city = "Atlanta"

result = Runner.run_sync(trip_agent, f"""Headed to {city} today. What weather should I expect and what is the 
                                       exact temperature right now? Also, what types of clothes should I pack""")
print(result.final_output)

