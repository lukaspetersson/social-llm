import requests
from bs4 import BeautifulSoup

def fetch_questions(page_url, carried_ec=0, carried_soc=0, page_num=1):
    data = {
        'page': page_num,
        'carried_ec': carried_ec,
        'carried_soc': carried_soc,
        'populated': '',
    }

    # Select the first option for each question on the page
    for i in range(1, 7):
        data[f'p{i}'] = 0

    response = requests.post(page_url, data=data)
    soup = BeautifulSoup(response.text, 'html.parser')

    form = soup.find('form', {'method': 'POST'})
    fieldset_blocks = form.find_all('fieldset', {'class': 'b1 pa2 mb1'})

    questions = []
    for i, fieldset_block in enumerate(fieldset_blocks, start=1):
        legend = fieldset_block.find('legend')
        question_text = legend.text.strip()
        questions.append(question_text)

    return questions

url = "https://www.politicalcompass.org/test/en"
all_questions = []

for i in range(1, 7):
    questions = fetch_questions(url, page_num=i)
    all_questions.extend(questions)

with open("data/political_compass_questions.txt", "w") as f:
    for question in all_questions:
        f.write(question)
        f.write("\n")
