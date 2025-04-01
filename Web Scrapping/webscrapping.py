from bs4 import BeautifulSoup
import requests
from lxml import etree
from collections import defaultdict
import json

scrap_data = defaultdict(dict)

url = 'https://www.javatpoint.com/python-mcq'
res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')
dom = etree.HTML(str(soup))

for i in range(1, 56):
    que = dom.xpath(f"//p[@class='pq'][{i}]/text()")
    code_snipet = dom.xpath(
        f"//p[@class='pq'][{i}]/following-sibling::div[1]/textarea/text()")
    que2 = dom.xpath(
        f'//p[@class="pq"][{i}]/following-sibling::div[@class="codeblock"]/following-sibling::p[1][not(contains(text(), ")"))]/text()'
    )
    mcqs = dom.xpath(f"//ol[@class='pointsa'][{i}]/li/text()")
    answers = dom.xpath(f"//div[@class='testanswer'][{i}]/p[1]/text()")
    explanation = dom.xpath(f"//div[@class='testanswer'][{i}]/p[2]/text()")

    if (code_snipet and que2):
        data = {
            "question": que[0],
            "code_snipet": code_snipet[0] if len(code_snipet) > 0 else '',
            "question2": que2[0] if len(que2) > 0 else '',
            "mcqs": mcqs,
            "answers": answers[0],
            "explanation": explanation[0]
        }
    elif (code_snipet):
        data = {
            "question": que[0],
            "code_snipet": code_snipet[0] if len(code_snipet) > 0 else '',
            "mcqs": mcqs,
            "answers": answers[0],
            "explanation": explanation[0]
        }
    else:
        data = {
            "question": que[0],
            "mcqs": mcqs,
            "answers": answers[0],
            "explanation": explanation[0]
        }
    scrap_data['question:' + str(i)] = data
print(dict(scrap_data))

with open('data.json', 'w') as wf:
    json.dump(dict(scrap_data), wf, indent=4)