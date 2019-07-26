from flask import Flask, jsonify
import socket


app = Flask(__name__)


@app.route('/')
def hello_ram():
    return jsonify("Hello pavan! I'm {}".format(socket.gethostname()))


app.run(host="0.0.0.0", port=5000)
