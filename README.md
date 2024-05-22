# Sentiment-Analysis-of-Discord-Messages
## CURRENTLY DOWN BECAUSE I DON'T HAVE MONEY TO KEEP THE DATABASE UP :(
#### Some files/filepaths/values are omitted due to privacy reasons!

This web application is a tracker for the amount of positive, negative, and neutral messages that are said in the #missed-connections channel of the Melee Online Discord. This can be adapted to any discord channel with any discord user.

### How it Works

To determine if a message is positive, negative, or neutral, I created a tensorflow model in python for sentiment analysis. This model takes in a .csv file of labeled data, consisting of the discord message and a sentiment label.

Another python script uses this model and scrapes the messages in the channel in real time, feeding them into the model and updating a counter for each respective sentiment. These counters are then put into another database. 

The web app pulls this database and displays these values in real time on the webpage.

### Technologies Used:

Languages: Python, HTML, CSS, Javascript

- Tensorflow, scikit-learn, and pandas used for creating the sentiment analysis model
- Flask used as the backend framework for the webapp
- Axios in JS for updating the counters in real time
- Google Cloud Storage for hosting the databases and running a virtual machine to run the real-time scraper script.
- Render.com used to host the web app
