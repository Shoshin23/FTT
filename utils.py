from twython import Twython
import re
import fasttext


token = "1154080303-71C0gdJhI5zmzcMVGJrzTPjRuxXdcWp2d7weZFS"
token_secret = "f5ZRZxzpVKkCdX2wkyyKxChaiX0csSmyFLzxM5AF4aULC"
consumer_key = "DXmpxxccoWxVPHzpR5PxyrIu5"
consumer_secret = "ilmcb9Rr4RIGa0zRkaCti3OUHDZ6JVLJ9nm9k7AzPbWHb1kBD1"

twitter = Twython(consumer_key,consumer_secret,token,token_secret)
lis = []
tweet_text = []
thefile = open('pred.txt', 'w')

# Function to return name, handle, total number of tweets and followers. 
def get_profile_details(handle):
	user_details = twitter.show_user(screen_name=handle)
	#preprocess the image and remove _normal from the image url.
	patt = re.compile('(\s*)_normal(\s*)')
	profile_image_url = patt.sub('',user_details['profile_image_url'])
	user_dict = {'Name':user_details['name'],'handle':handle,'profile_image_url':profile_image_url,'followers_count':user_details['followers_count']}

	return user_dict 

def get_tweets_text(handle):

	if(lis and tweet_text):  #use 'and' instead of '&&'. Silly. 
		del lis[:]
		del tweet_text[:]

	user_timeline = twitter.get_user_timeline(screen_name=handle,count=1)
	lis.append(user_timeline[0]['id'])
	for i in range(0, 16):
		user_timeline = twitter.get_user_timeline(screen_name=handle, count=200, include_rts=False, max_id=lis[-1])
		for tweet in user_timeline:
			cleaned_tweet = re.sub(r"http\S+", "", tweet['text'])
			tweet_text.append(cleaned_tweet)
			lis.append(tweet['id'])
	predict_sentiment()
	# for tweet in tweet_text:
	# 	thefile.write("%s\n" %tweet)
	# return thefile
	#print("done writing tweets to the file!")


def predict_sentiment():
	if tweet_text:
		tweet_sample = tweet_text[:10]
		print(tweet_sample)
		classifier = fasttext.load_model('model3.bin',encoding='utf-8')
		labels = classifier.predict_proba(tweet_sample)
		print(labels)
	else:
		print("No tweets to predict!")
