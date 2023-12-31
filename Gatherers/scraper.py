import requests
import json
import re


def scrapePast(cid):
    x = ''
    headers = {
        '' #discord auth token omitted
    }
    r = requests.get(f'https://discord.com/api/v9/channels/{cid}/messages?limit=100', headers=headers)
    js = json.loads(r.text)


    messageFile = open('../Datasets/main.csv', 'w', encoding='utf-8')
    newestID = js[0]['id']
    for i in js[::-1]:
        if i['id'] != newestID:
            print(i['content'], file=messageFile)
    messageFile.close()
    x = 240
    while x >= 0:
        mid = js[-1]['id']
        r = requests.get(f'https://discord.com/api/v9/channels/{cid}/messages?limit=100&before={mid}', headers=headers)
        js = json.loads(r.text)
        messageFile = open('../Datasets/main.csv', 'a', encoding='utf-8')
        for i in js[::-1]:
            if i['id'] != newestID:
                print(i['content'], file=messageFile)
            if i['id'] == '': #discord channel path omitted
                break;
        messageFile.close()
        x -= 1


def filter():
    # Replace " with '
    with open('../Datasets/main.csv', 'r', encoding='utf-8') as file:
        text = file.read()
    text = text.replace('"', "'") 
    with open('../Datasets/main.csv', 'w', encoding='utf-8') as file:
        file.write(text)
    # Add quotes and a , at the end of each line
    with open('../Datasets/main.csv', 'r', encoding='utf-8') as file:
        text = file.readlines()
    quotes = ['"' + line.strip() + '",' for line in text]
    with open('../Datasets/main.csv', 'w', encoding='utf-8') as new_file:
        new_file.write('\n'.join(quotes))
        new_file.close()
    # Remove mentions from each line
    with open('../Datasets/main.csv', 'r', encoding='utf-8') as file:
        text = file.read()
    text = re.sub(r'<@\d*> ', '', text)
    text = re.sub(r'<@\d*>', '', text)
    with open('../Datasets/main.csv', 'w', encoding='utf-8') as new_file:
        new_file.write(text)
        new_file.close()

scrapePast('') #discord channel path omitted
filter()

