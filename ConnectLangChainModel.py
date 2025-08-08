### connecting to an AI agent 

### Set up
import os 
import pandas as pd 
from IPython.display import Markdown, HTML, display

#leveraging langchain

from langchain.schema import HumanMessage
from langchain_openai import AzureChatOpenAI

model = AzureChatOpenAI(
    openai_api_version="2024-04-01-preview",
    azure_deployment="gpt-4-1106",
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
)

# Preparing prompt

message = HumanMessage(
    content="Translate this sentence from English "
    "to French and Spanish. I like red cars and "
    "blue houses, but my dog is yellow."
)

# Engaging the model to receive response

model.invoke([message])