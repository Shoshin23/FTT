
from flask import Flask, render_template,request,redirect
from twitter import *
import requests
from requests_oauthlib import OAuth1Session

import json
app = Flask(__name__, static_folder='templates')
token = "1154080303-71C0gdJhI5zmzcMVGJrzTPjRuxXdcWp2d7weZFS"
token_secret = "f5ZRZxzpVKkCdX2wkyyKxChaiX0csSmyFLzxM5AF4aULC"
consumer_key = "DXmpxxccoWxVPHzpR5PxyrIu5"
consumer_secret = "ilmcb9Rr4RIGa0zRkaCti3OUHDZ6JVLJ9nm9k7AzPbWHb1kBD1"
# t = Twitter(
#     auth=OAuth(token, token_secret, consumer_key, consumer_secret))

tweets_text = []

twitter = OAuth1Session(consumer_key,client_secret=consumer_secret, resource_owner_key=token, resource_owner_secret=token_secret)
status_url = "https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name="

def get_tweets_text(tweets_json):
## Get the text from the tweets and write it to a file. ##
	for i in range(len(tweets_json)):
		tweets_text.append(tweets_json[i]['text'])
		print(tweets_text)
		print(len(tweets_text))


@app.route('/') #index.
def index():
	return render_template('index.html')

@app.route('/result',methods=['POST'])
def result():
	handle = request.form['twitter-handle']
	# tl = t.statuses.user_timeline(screen_name=handle)
	tweets = twitter.get(status_url+handle+'&count=200&include_rts=false&exclude_replies=true')
	tweets_json = tweets.json()
	get_tweets_text(tweets_json)
	#print(tweets_json[0]['text'])
	return redirect('/')
if __name__ == '__main__':
	app.run()

