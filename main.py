from flask import Flask, render_template,request,redirect
from twitter import *
import json
app = Flask(__name__, static_folder='templates')
token = "1154080303-71C0gdJhI5zmzcMVGJrzTPjRuxXdcWp2d7weZFS"
token_secret = "f5ZRZxzpVKkCdX2wkyyKxChaiX0csSmyFLzxM5AF4aULC"
consumer_key = "DXmpxxccoWxVPHzpR5PxyrIu5"
consumer_secret = "ilmcb9Rr4RIGa0zRkaCti3OUHDZ6JVLJ9nm9k7AzPbWHb1kBD1"
t = Twitter(
    auth=OAuth(token, token_secret, consumer_key, consumer_secret))

@app.route('/') #index.
def index():
	return render_template('index.html')

@app.route('/result',methods=['POST'])
def result():
	handle = request.form['twitter-handle']
	tl = t.statuses.user_timeline(screen_name=handle)
	extract_text(tl)
	return redirect('/')
if __name__ == '__main__':
	app.run()

