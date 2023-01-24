import time
import redis
from flask import Flask

app = Flask(__name__)  # set name of the application package

cache = redis.Redis(host='redis', port=6379) # create connection to redis

def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)

@app.route('/') # entry point for home
def hello():
    count = get_hit_count()
    return 'Hello World! I have been seen {} times.\n'.format(count)