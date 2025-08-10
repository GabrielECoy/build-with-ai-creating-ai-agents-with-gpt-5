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
from agents import Agent, Runner, function_tool, ModelSettings
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
# # LESSON 3 (Steer agent behavior and reasoning)
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
        "You help travelers plan activities to do while on vacation but you check the weather first in real-time."
        "When asked about weather, call the get_weather_forecast tool."
        "Make sure you have access to real-time weather data to make your recommendations."
        "Make sure to pick activities that solo travlers will enjoy. Use web search if necessary."
    ),
    model="gpt-5",
    tools=[get_weather_forecast],
    # ---------- Lesson 3: steer behavior----------
    model_settings=ModelSettings(
        reasoning={"effort": "high"}   # minimal | low | medium | high 
    )
)

city = "Atlanta"

result = Runner.run_sync(trip_agent, f"""Headed to {city} today. What weather should I expect and what is the 
                                       exact temperature right now? What things do you recommend I do while visiting the city?""")
print(result.final_output)

