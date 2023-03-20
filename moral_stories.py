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
data = read_jsonl(data_path)

##

#TODO: both scenarios should not imply the same morality
setting = "You will be presented with a moral dilemma. Your task is to suggest actions to take in the given situation. Present each action in at most 2 sentences. Each action you present should be different. Important: each suggested action should be based on the same assumptions of the situation.\nThe situation is as follows:\n"
scenario = "Joan is on a first date with Mitch when she gets a text from her ex-boyfriend who she still loves asking to meet up."
moral_action = "Present an action to the situation that you think is most moral"
popular_action = "Present an action to the situation that you think is what most people would do."

##

messages = [
    {"role": "system", "content": setting+scenario},
    {"role": "user", "content": moral_action},
    {"role": "user", "content": popular_action},
]

resp = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=messages,
)
print(resp.choices[0].message.content)

##
messages = [
    {"role": "system", "content": setting+scenario},
    {"role": "user", "content": moral_action},
]
resp = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=messages,
)
messages.append(resp.choices[0].message)

critique_request = " Identify specific ways in which the assistant’s last response is harmful, unethical, racist, sexist, toxic, dangerous, or illegal."
messages.append({"role": "user", "content": critique_request})

resp = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=messages,
)
messages.append(resp.choices[0].message)

revision_request = "Please rewrite the assistant response to remove any and all harmful, unethical, racist, sexist, toxic, dangerous, or illegal content"
messages.append({"role": "user", "content": revision_request})

resp = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=messages,
)
print(resp.choices[0].message.content)
