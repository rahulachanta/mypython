import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os
import json

# Load environment variables from .env file
load_dotenv()

# Get the OpenAI API key from environment variables
#open the config file and read the API Key
with open('config.json') as config_file:
    config = json.load(config_file)
    open_api_key = config['open_api_key']

# Initialize the OpenAI client
client = OpenAI(api_key=open_api_key)

#App title
st.title("AI Text Generator with OpenAI API")

#User input
user_input = st.text_area("Enter your prompt here:")

with st.sidebar:
    st.header("Settings")
    
tone = st.selectbox(
    "Choose Tone",
    ["Professional","Friendly","Funny"]
)

#Button
if st.button("Generate Text"):
    if user_input:
        # Call the OpenAI API to generate text
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role":"system",
                    "content":f"You are an {tone} AI assistant"
                },
                {
                    "role": "user",
                    "content": user_input
                }
            ]
        )

        #Extract AI Response
        ai_response = response.choices[0].message.content

        # Display the generated text
        st.subheader("AI Response:")
        st.write(ai_response)
    else:
        st.warning("Please enter a prompt to generate text.")
