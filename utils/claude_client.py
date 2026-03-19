import anthropic
import os
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

def get_api_key():
    try:
        return st.secrets["ANTHROPIC_API_KEY"]
    except:
        return os.getenv("ANTHROPIC_API_KEY")

client = anthropic.Anthropic(
    api_key=get_api_key()
)

def call_claude(system_prompt, user_message, max_tokens=1000):
    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=max_tokens,
        system=system_prompt,
        messages=[
            {"role": "user", "content": user_message}
        ]
    )
    return response.content[0].text