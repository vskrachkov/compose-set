from flask import Flask
from redis import Redis

DEBUG = True

app = Flask(__name__)
redis = Redis(host='redis', port=6379)

@app.route('/api')
def index():
    hits = redis.incr('hits')
    return f'Hello from flask app: {hits} ###'

@app.route('/api/<int:number>')
def num(number):
    return f'Your num is {number}'


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=DEBUG)
