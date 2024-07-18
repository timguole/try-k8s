from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def hello():
	request_method = request.environ.get('REQUEST_METHOD')
	remote_addr = request.environ.get('REMOTE_ADDR')
	remote_port = request.environ.get('REMOTE_PORT')
	server_name = request.environ.get('SERVER_NAME')
	server_port = request.environ.get('SERVER_PORT')
	server_protocol = request.environ.get('SERVER_PROTOCOL')

	return f'''Hello, world! Welcome to Flask!
request_method: {request_method}
remote_addr: {remote_addr}
remote_port: {remote_port}
server_name: {server_name}
server_port: {server_port}
server_protocol: {server_protocol}
'''
