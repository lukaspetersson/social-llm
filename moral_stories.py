from datasets import load_dataset
import openai
from dotenv import dotenv_values
import json

env_var = dotenv_values(".env")
openai_token = env_var["OPENAI_TOKEN"]
openai.api_key = openai_token


##

def read_jsonl(file_path):
    data = []
    with open(file_path, 'r') as file:
        for line in file:
            json_object = json.loads(line)
            data.append(json_object)
    return data

##
data_path = "./data/moral_stories_full.jsonl"
read_jsonl(data_path)[:3]

##

#TODO: use n=2 instead?
#TODO: scenarios should make the same assumptions (not comparable otherwise)
#TODO: both scenarios should not imply the same morality
instruction = "Generate 2 different actions to the following moral scenarios:"
scenario = "Joan is on a first date with Mitch when she gets a text from her ex-boyfriend who she still loves asking to meet up."

messages = [
    {"role": "system", "content": instruction},
    {"role": "user", "content": scenario},
]

resp = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=messages,
)

print(resp.choices[0].message.content)

