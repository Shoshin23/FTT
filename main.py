
from flask import Flask, render_template,request,redirect
from utils import * #import shit from the utils file. 
import json
import os
app = Flask(__name__, static_folder='templates')



@app.route('/') #index.
def index():
	return render_template('index.html')

@app.route('/result',methods=['POST'])
def result():
	handle = request.form['twitter-handle']
	get_tweets_text(handle)
	return redirect('/')

@app.url_defaults
def hashed_url_for_static_file(endpoint, values):
    if 'static' == endpoint or endpoint.endswith('.static'):
        filename = values.get('filename')
        if filename:
            if '.' in endpoint:  # has higher priority
                blueprint = endpoint.rsplit('.', 1)[0]
            else:
                blueprint = request.blueprint  # can be None too

            if blueprint:
                static_folder = app.blueprints[blueprint].static_folder
            else:
                static_folder = app.static_folder

            param_name = 'h'
            while param_name in values:
                param_name = '_' + param_name
            values[param_name] = static_file_hash(os.path.join(static_folder, filename))
            
def static_file_hash(filename):
  return int(os.stat(filename).st_mtime) # or app.config['last_build_timestamp'] or md5(filename) or etc...


if __name__ == '__main__':
	app.run()

