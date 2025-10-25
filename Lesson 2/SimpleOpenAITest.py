from dotenv import load_dotenv, find_dotenv

dotenvfile = find_dotenv()
_ = load_dotenv(dotenvfile) 

import os
os.system('cls') # Windows
os.system('clear') # Linux

from openai import OpenAI
token = os.environ["OPENAI_API_KEY"]
UsingGitHub = (token[:10]=="github_pat")
print (f"Token: {token} - Using GitHub: {UsingGitHub}")

endpoint = "https://models.github.ai/inference"
model = "gpt-5" # "gpt-4o" # "openai/gpt-4o"

def main():
    if UsingGitHub:
        client = OpenAI(
            base_url=endpoint,
            api_key=token,
        )
    else:
        client = OpenAI(
                api_key=token,
        )

    response = client.chat.completions.create(
        model=model,
        max_tokens=100, # Reduced token limit to try avoid you exceeded your current quota error in OpenAI
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "What is the capital of France?"}
        ]
    )

    print(f"Response from model {model} is: ",response.choices[0].message.content)

from pprint import pprint
if __name__ == "__main__":
    try:
        main()
    except Exception as err:
        print(f"The sample encountered an error:\n{err}")