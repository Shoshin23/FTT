
from flask import Flask, render_template,request,redirect
from utils import * #import shit from the utils file. 
import json

app = Flask(__name__, static_folder='templates')



@app.route('/') #index.
def index():
	return render_template('index.html')

@app.route('/result',methods=['POST'])
def result():
	handle = request.form['twitter-handle']
	get_tweets_text(handle)
	return redirect('/')


if __name__ == '__main__':
	app.run()

