import requests
import json
import re


def scrapePast(cid):
    x = ''
    headers = {
        '' #insert auth token of discord account here
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
            if i['id'] == '726108563193462934':
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

scrapePast('726108367478849577')
filter()



"""
{'id': '1166161254226870282', 'type': 0, 'content': 'thats how you know its bad', 'channel_id': '726108367478849577', 'author': {'id': '357154426621788160', 'username': 'drew_burger', 'avatar': 'a9a05ac825c12398e14cad9b63154b27', 'discriminator': '0', 
'public_flags': 64, 'premium_type': 0, 'flags': 64, 'banner': None, 'accent_color': 
None, 'global_name': 'drew', 'avatar_decoration_data': None, 'banner_color': None}, 
'attachments': [], 'embeds': [], 'mentions': [], 'mention_roles': [], 'pinned': False, 'mention_everyone': False, 'tts': False, 'timestamp': '2023-10-23T23:48:29.236000+00:00', 'edited_timestamp': None, 'flags': 0, 'components': []}
"""
