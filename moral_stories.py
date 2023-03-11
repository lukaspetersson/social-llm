from datasets import load_dataset
import openai
from dotenv import dotenv_values

env_var = dotenv_values(".env")
openai_token = env_var["OPENAI_TOKEN"]
openai.api_key = openai_token

##

subs = ['full', 'cls-action-lexical_bias', 'cls-action-minimal_pairs', 'cls-action-norm_distance', 'cls-action+context-lexical_bias', 'cls-action+context-minimal_pairs', 'cls-action+context-norm_distance', 'cls-action+context+consequence-lexical_bias', 'cls-action+context+consequence-minimal_pairs', 'cls-action+context+consequence-norm_distance', 'cls-action+norm-lexical_bias', 'cls-action+norm-minimal_pairs', 'cls-action+norm-norm_distance', 'cls-consequence+action-lexical_bias', 'cls-consequence+action-minimal_pairs', 'cls-consequence+action-norm_distance', 'cls-consequence+action+context-lexical_bias', 'cls-consequence+action+context-minimal_pairs', 'cls-consequence+action+context-norm_distance', 'gen-action$context-norm_distance', 'gen-action$context+consequence-norm_distance', 'gen-consequence$action-norm_distance', 'gen-consequence$action+context-norm_distance', 'gen-norm$actions-norm_distance', 'gen-norm$actions+context-norm_distance', 'gen-norm$actions+context+consequences-norm_distance']
s = []
for sub in subs:
    try:
        dataset = load_dataset("demelin/moral_stories", sub)
        s.append(sub)
    except:
        pass


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

