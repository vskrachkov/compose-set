from flask import Flask
from redis import Redis

DEBUG = True

REDIS = {
    'LOCATION': [
        ('redis', 6379)
    ]
}

app = Flask(__name__)
redis = Redis(host=REDIS['LOCATION'][0][0], port=REDIS['LOCATION'][0][1])

@app.route('/api')
def index():
    hits = redis.incr('hits')
    return f'Hello from flask app: {hits} ###'

@app.route('/api/<int:number>')
def num(number):
    return f'Your num is {number}'


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=DEBUG)
