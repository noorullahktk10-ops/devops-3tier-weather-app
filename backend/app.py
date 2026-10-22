# -*- coding: utf-8 -*-
from flask import Flask, jsonify
from flask_cors import CORS
import redis
import json

app = Flask(__name__)
CORS(app)

r = redis.Redis(host='redis', port=6379, decode_responses=True)

@app.route('/api/weather/<city>')
def weather(city):
    cached = r.get(city)
    if cached:
        return jsonify(json.loads(cached))
    data = {"city": city, "temp": "25 C", "status": "Sunny - DevOps Project Running"}
    r.setex(city, 60, json.dumps(data))
    return jsonify(data)

@app.route('/')
def home():
    return "Backend is running!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
