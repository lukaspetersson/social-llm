import json

def read_jsonl(file_path):
    data = []
    with open(file_path, 'r') as file:
        for line in file:
            json_object = json.loads(line)
            data.append(json_object)
    return data

data_path = "./data/moral_stories_full.jsonl"
data = read_jsonl(data_path)

file = open("./data/dilemma_prompts.jsonl", "w")

for i, entry in enumerate(data):
    norm = entry["norm"]
    dilemma = entry["situation"]
    prompt = '{"prompt": "Generate a moral dilemma that highlights the following norm: ' + norm + '", "completion": "' + dilemma + '"}'
    file.write(prompt)
    if i != len(data)-1:
        file.write("\n")
file.close()

