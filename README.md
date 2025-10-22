## Notes
I used a Code space, but the course was expecting to clone the repo in my local drive
Steps for creating a venv:
- python -m venv venv
- source venv/bin/activate   # macOS/Linux
- venv\Scripts\activate      # Windows
- pip install -r requirements.txt

OpenAI API key — sign up at https://platform.openai.com/signup 
from: https://platform.openai.com/api-keys
Name: Key for the Creating AI Agents with GPT‑5 course    
Secret Key: sk-...xEQA
Created: Oct 20, 2025
Last used: Never
Created by: Gabriel Coy
Permissions: All

OpenAI returned 'insufficient_quota' (there is probably no API allowance for free accounts). Claude recommended the following solution:
Go to https://platform.openai.com/account/billing
Add a payment method (even if you have free credits)
Generate a new API key
Try again

I tried to use use GitHub models OpenAI 5.0 (from https://github.com/marketplace/models/azure-openai/gpt-5/playground), but GPT5 models were returning "not available" in GitHub models, even when testing in the UI
Note: Because I was using a GitHub models OpenAI key, I changed the instanciation of OpenAI to point to Azure OpenAI endpoint. I finally made it conditinal, based on the key pattern
endpoint = "https://models.github.ai/inference" # or "https://models.inference.ai.azure.com"
client = OpenAI(
  api_key=os.environ['OPENAI_API_KEY'],base_url=endpoint) #model="openai/gpt-5"

WeatherAPI key — used for the real-time weather tool, sign up at https://www.weatherapi.com
See \\CoyTeraStation\Personal\Datos\Accesos y Subscripcion\Accesos\WeatherAPI
I used a Code space for the exercises, but course was expecting to use local drive
macOS/Linux
export OPENAI_API_KEY="your_api_key"
export WEATHER_API_KEY="your_api_key"
Windows PowerShell
setx OPENAI_API_KEY "your_api_key"       
setx OPENAI_API_KEY "your_api_key"

To import the Key I added a .env file with the OPENAI_API_KEY value in the default folder os.getcwd()
Default folder: 
Note: I added .env in .gitignore so the key was not added to source control

Used the following to load the value
print(os.getcwd())
from dotenv import load_dotenv
load_dotenv()

To confirm the value was there I used:
import dotenv_values
print(len(dotenv_values()))
for key, value in dotenv_values().items():
    print(f"{key}: {value}")

To clean the output of the cell before commiting into git
from IPython.display import clear_output
clear_output()

# Build with AI: Creating AI Agents with GPT‑5
This repository contains the Python code examples from the LinkedIn Learning course **Build with AI: Creating AI Agents with GPT‑5**.

![Build with AI: Creating AI Agents with GPT-5](https://github.com/keshawillz/build-with-ai-creating-ai-agents-with-gpt-5/blob/main/course_image2.png)

You’ll learn how to:
- Build agents that can call tools and take action
- Steer GPT-5 output using verbosity and reasoning settings
- Extend agents with custom tools for more capabilities

## Requirements
- Python 3.9+
- An [OpenAI API key](https://platform.openai.com/account/api-keys)
- A [Weather API key](https://www.weatherapi.com/my/)

## Setup

1. **Clone this repo** (or download the files).
2. **Create and activate a virtual environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate   # macOS/Linux
    venv\Scripts\activate      # Windows
    ```
3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
4. **Set your OpenAI API key or place in .env file**:
    ```bash
    export OPENAI_API_KEY="your_api_key"      # macOS/Linux
    setx OPENAI_API_KEY "your_api_key"        # Windows PowerShell
    ```
5. **Set your Weather API key or place in .env file**:
    ```bash
    export WEATHER_API_KEY="your_api_key"      # macOS/Linux
    setx OPENAI_API_KEY "your_api_key"        # Windows PowerShell
    ```

## Running the Examples

Run the main demo script to see all lessons in action:

```bash
python agent.py

