import responder
from datetime import datetime
import socket

api = responder.API()

@api.route("/")
async def root(req, resp):
    resp.text = f"Hello Micro Service Academy!\n" + \
    			f"Time Now: {datetime.now()}\n" + \
    			f"Hostname: {socket.gethostname()}"

@api.route("/name/{name}")
async def hello_name(req, resp, *, name):
    resp.text = f"Hello {name}!"

@api.route("/index")
async def index(req, resp):
    resp.text = open('index.html').read()

if __name__ == '__main__':
	api.run(port=5000)