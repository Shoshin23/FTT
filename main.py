
from twython import Twython
from flask import Flask, render_template,request,redirect
import requests
from requests_oauthlib import OAuth1Session
import time


import json
app = Flask(__name__, static_folder='templates')
token = "1154080303-71C0gdJhI5zmzcMVGJrzTPjRuxXdcWp2d7weZFS"
token_secret = "f5ZRZxzpVKkCdX2wkyyKxChaiX0csSmyFLzxM5AF4aULC"
consumer_key = "DXmpxxccoWxVPHzpR5PxyrIu5"
consumer_secret = "ilmcb9Rr4RIGa0zRkaCti3OUHDZ6JVLJ9nm9k7AzPbWHb1kBD1"
# t = Twitter(
#     auth=OAuth(token, token_secret, consumer_key, consumer_secret))

tweets_text = []

#twitter = OAuth1Session(consumer_key,client_secret=consumer_secret, resource_owner_key=token, resource_owner_secret=token_secret)
status_url = "https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name="

twitter = Twython(consumer_key,consumer_secret,token,token_secret)
lis = []
tweet_text = []
thefile = open('pred.txt', 'w')

# def get_tweets_text(tweets_json):
# ## Get the text from the tweets and write it to a file. ##
# 	for i in range(len(tweets_json)):
# 		tweets_text.append(tweets_json[i]['text'])
# 		print(tweets_text)
# 		print(len(tweets_text))

def get_tweets_text2(handle):
	user_timeline = twitter.get_user_timeline(screen_name=handle,count=1)
	lis.append(user_timeline[0]['id'])
	for i in range(0, 16):
		user_timeline = twitter.get_user_timeline(screen_name=handle, count=200, include_rts=False, max_id=lis[-1])
		for tweet in user_timeline:
			#print(tweet['text'])
			tweet_text.append(tweet['text'])
			lis.append(tweet['id'])
	for tweet in tweet_text:
		thefile.write("%s\n" %tweet)
	print("done writing tweets to the file!")


@app.route('/') #index.
def index():
	return render_template('index.html')

@app.route('/result',methods=['POST'])
def result():
	handle = request.form['twitter-handle']
	del lis[:]
	del tweet_text[:]
	get_tweets_text2(handle)
	return redirect('/')


if __name__ == '__main__':
	app.run()

