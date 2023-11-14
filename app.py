from flask import Flask, render_template, jsonify
import pandas as pd
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "" #auth file path ommited

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get')
def get():
    df = pd.read_csv('') #dataset path omitted
    values = {
        'positive': int(df.at[0, "Value"]), 
        'negative': int(df.at[1, "Value"]), 
        'neutral': int(df.at[2, "Value"])
    }
    return jsonify(values)

@app.route('/about')
def about():
    return render_template('about.html')

