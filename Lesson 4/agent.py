"""
Build with AI: Creating AI Agents with GPT-5
All examples use Python and the OpenAI client.

Prereqs:
  pip install openai
  pip install python-dotenv
  export OPENAI_API_KEY="sk-..."
"""
import os
from openai import OpenAI
from dotenv import load_dotenv, find_dotenv
from agents import Agent, Runner, function_tool
from dataclasses import dataclass

# read local .env file
_ = load_dotenv(find_dotenv()) 

# retrieve OpenAI API key
client = OpenAI(
  api_key=os.environ['OPENAI_API_KEY']  
)

if not api_key:
   raise ValueError("OPENAI_API_KEY not found in local .env file")

# # ---------------------------------------------------------------------------
# # LESSON 2 (Build a Basic Agent with Tool Calling)
# # ---------------------------------------------------------------------------
@dataclass
class PlotInfo:
    transcript: str
    location: str
    attendee_count: str

@function_tool
def generate_summary_tool(text: str) -> str:
    """
    Summarize a meeting
    """
    lines = [ln.strip() for ln in text.splitlines() if ln.strip()]
    if not lines:
        return "No content provided."
    head = lines[0][:120]
    return f"{head} … (summary generated)"

agent = Agent(
    name="Meeting Summary Agent",
    instructions="You are a helpful assistant. Use the tool to summarize meeting transcripts.",
    model="gpt-5",
    tools=[generate_summary_tool]
)

result = Runner.run_sync(agent, f"Summarize this meeting transcript: {transcript_text}")
print(result.final_output)