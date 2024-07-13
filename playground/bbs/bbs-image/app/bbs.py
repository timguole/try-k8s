from flask import Flask
from flask import request
from flask import current_app, g
import redis
import os

app  = Flask(__name__)
app.config['rc'] = redis.Redis(host=os.environ.get('BBS_REDIS_HOST', 'redis'), \
		port=int(os.environ.get('BBS_REDIS_PORT', 6379)), \
		db = 0, \
		decode_responses=True)

@app.route('/')
def index():
	return 'Post to /post (key=, value=) and get from /list\n'


@app.route('/post', methods = ['POST'])
def post_data():
	k = request.form['key']
	v = request.form['value']
	if k is None or v is None:
		return 'invalid key or value\n'
	current_app.config['rc'].set(k, v)
	return f'set {k} : {v}\n'


@app.route('/list', methods = ['GET'])
def list_data():
	kv = []
	rc = current_app.config['rc']
	for k in rc.keys():
		v = rc.get(k)
		kv.append(f'{k}: {v}')
	return 'Data:\n' + '\n'.join(kv) + '\n'

