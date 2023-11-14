import keras
import tensorflow as tf
import pickle5 as pickle
import numpy as np
import pandas as pd
import requests
import json
import time
from google.cloud import storage

def scrapePresent(cid):
    headers = {
        'authorization': 'NzYzMjA4ODU4NzIxMzIwOTkx.Gzf_Vj.qHjXRv25xHGbyaDxef8zYUha6mGhvrt2D_62bo'
    }
    r2 = requests.get(f'https://discord.com/api/v9/channels/{cid}/messages?limit=1', headers=headers)
    js2 = json.loads(r2.text)
    i = js2[0]
    return i

model = keras.models.load_model('./SA_Model/missed_connections.h5')
with open('./SA_Model/tokenizer.pickle', 'rb') as handle:
    tokenizer = pickle.load(handle)

def predict(text):
    seq = tokenizer.texts_to_sequences([text])
    seq = tf.keras.preprocessing.sequence.pad_sequences(seq, maxlen=76)
    rating = model.predict(seq)[0]
    if np.argmax(rating) == 0:
        return 'Negative'
    elif np.argmax(rating) == 1:
        return 'Neutral'
    else:
        return 'Positive'
    
current = 0
positive, negative, neutral = 0, 0, 0
variables = pd.read_csv('gs://mcst/variables.csv')
cli = storage.Client()
bucket = cli.bucket('mcst')
blob = bucket.blob('variables.csv')
while True:
    i = scrapePresent('726108367478849577')
    if i['id'] != current:
        txt = i['content'].replace('\n', " ")
        if predict(txt) == 'Negative': 
            negative += 1
            variables.at[1, "Value"] = negative
        elif predict(txt) == 'Positive': 
            positive += 1
            variables.at[0, "Value"] = positive
        else: 
            neutral += 1
            variables.at[2, "Value"] = neutral
    variables.to_csv('./variables.csv')
    blob.upload_from_filename('./variables.csv')
    current = i['id']
    time.sleep(3)


