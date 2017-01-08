from sitestatus import app
import requests
@app.route('/')
def index():
	r = requests.get('https://api.github.com/events')
	return r.text