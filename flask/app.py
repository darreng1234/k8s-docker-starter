from flask import Flask, request
import os
import time

app = Flask(__name__)

memory_consumption = []

@app.route('/')
def index():
    global memory_consumption
    memory_consumption.append([0] * 142857)
    return "Memory usage increasing!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)