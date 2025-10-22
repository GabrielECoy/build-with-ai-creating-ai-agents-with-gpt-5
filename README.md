## Notes
I used a Code space, but the course was expecting to clone the repo in my local drive
Steps for creating a venv:
- python -m venv venv
- source venv/bin/activate   # macOS/Linux
- venv\Scripts\activate      # Windows
- pip install -r requirements.txt

OpenAI API key — sign up at https://platform.openai.com/signup
Note:  I may have been able to use a Key generated at:OpenAI gpt-5 · GitHub Models (more info at "Hands-On AI: Introduction to Retrieval-Augmented Generation (RAG) - Yujian Tang"), but I used one from API keys - OpenAI API
    
from: https://platform.openai.com/api-keys
Name: Key for the Creating AI Agents with GPT‑5 course    
Secret Key: sk-...xEQA
Created: Oct 20, 2025
Last used: Never
Created by: Gabriel Coy
Permissions: All

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
Note: If I were not using an OpenAI key, but a GitHub models OpenAI key, I would have changed the instanciation of OpenAI below to point to Azure OpenAI endpoint

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

