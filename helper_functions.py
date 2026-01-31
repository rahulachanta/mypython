# helper_functions.py

import openai

Def authenticate(api_key = None):
	global client
	Try:
		load_dotenv(.env', override=True)
		openai_api_key = os.getenv('OPEN_API_KEY')
		client = OpenAI(api_key=openai_api_key)
	except:
		if api_key == None:
			print("Warning: An OpenAI API Key is required to use AI Model functions.
				Please provide	the key by calling`authenticate(openai_api_key)`
				or ensure it is specified in the `.env` file as 'OPENAI_API_KEY' 				If you set it in the `.env` file, call `authenticate()` or 					reload the package to proceed.")
			return
	else:
		client = OpenAI(api_key=api_key)
	

Def print_llm_response(prompt):
	"""This function takes as input a prompt, which must be string enclosed in quotation marks, and passes it to OpenAI's GPT-4o-mini model. The function  then prints the response of the model.
"""
	try:
		if not isinstance(prompt, str):
			raise ValueError("Input must be a string enclosed in quotes.")
		completion = client.chat.completions.create(
			model="gpt-4o-mini",
			messages=[
				{
					"role":"system"
					"content":"Your a helpful but terse AI assistant  who gets straight  to the point.",
	},
	{"role":"user","content":prompt},
],
Temperature=0.0,
)
response=completion.choices[0].message.content
print(response)
Execpt TypeError as e:
	print("Error:", str(e))

Def get_llm_response(prompt):
	"""This function takes as input a prompt, which must be a string enclosed in quotation marks, and passes it to OpenAI's GPT-4o-mini model. The function then saves the response of the model as a string."""
Completion =client.chat.completions.create(
	model="gpt-4o-mini",
	messages=[
		{
			"role":"system",
			"content": "You are helpful but terse AI assistant who gets straight to the point.",
},
{"role":"user", "content":prompt},
],
Temperature =0.0,
)
response=completion.choices[0].message.content
Return response 



def print_llm_response(prompt, model="gpt-3.5-turbo"):
    response = openai.ChatCompletion.create(
        model=model,
        messages=[{"role": "user", "content": prompt}]
    )
    return response['choices'][0]['message']['content']
