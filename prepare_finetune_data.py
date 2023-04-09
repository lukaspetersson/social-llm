import json

def read_jsonl(file_path):
    data = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            json_object = json.loads(line)
            data.append(json_object)
    return data

data_path = "./data/moral_stories_full.jsonl"
data = read_jsonl(data_path)

with open("./data/dilemma_prompts.jsonl", "w", encoding='utf-8') as file:
    for i, entry in enumerate(data):
        norm = entry["norm"]
        dilemma = entry["situation"]
        prompt_dict = {
            "prompt": f"Generate a moral dilemma that highlights the following norm: {norm}",
            "completion": dilemma
        }
        prompt_json = json.dumps(prompt_dict)
        file.write(prompt_json)
        if i == 1000:
            break
        else:
            file.write("\n")
