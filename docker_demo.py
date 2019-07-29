from flask import Flask, jsonify
from redis import RedisError, Redis
import socket


app = Flask(__name__)
redis = Redis(host="redis", db=0, socket_connect_timeout=2, socket_timeout=2)


@app.route('/')
def hello_ram():
    i_am = socket.gethostname()
    try:
        visits = redis.incr(i_am)
    except RedisError:
        visits = 0
    return jsonify("Hi Ram, I'm {}. I've been seen {} times".format(
        i_am, visits))


app.run(host="0.0.0.0", port=5000)
