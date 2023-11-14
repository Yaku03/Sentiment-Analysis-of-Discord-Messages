from flask import Flask, render_template, jsonify
import pandas as pd
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "diesel-polymer-404717-23549847daf2.json"

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get')
def get():
    df = pd.read_csv('gs://mcst/variables.csv')
    values = {
        'positive': int(df.at[0, "Value"]), 
        'negative': int(df.at[1, "Value"]), 
        'neutral': int(df.at[2, "Value"])
    }
    return jsonify(values)

@app.route('/about')
def about():
    return render_template('about.html')

