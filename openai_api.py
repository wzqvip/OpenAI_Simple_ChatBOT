import openai
import os

def initialize_api():
    openai.api_key = os.environ.get("OPENAI_API_KEY")
    if not openai.api_key:
        raise ValueError("Please set the OPENAI_API_KEY environment variable to use the OpenAI API.")

def generate_response(prompt, model="text-davinci-002", max_tokens=150):
    response = openai.Completion.create(
        engine=model,
        prompt=prompt,
        max_tokens=max_tokens,
        n=1,
        stop=None,
        temperature=0.7,
    )

    return response.choices[0].text.strip()
