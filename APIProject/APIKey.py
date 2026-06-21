import os
import json
from openai import OpenAI

#get the current working directory
current_directory = os.getcwd()
print("Current working directory:", current_directory)

#open the config file and read the API Key
with open('config.json') as config_file:
    config = json.load(config_file)
    open_api_key = config['open_api_key']

#print("Open API Key:", open_api_key)
client = OpenAI(api_key=open_api_key)

models = client.models.list()
""" 
for model in models:
    print(model.id)
 """

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": "Explain APIs simply"}]
)

print(response.choices[0].message.content)
