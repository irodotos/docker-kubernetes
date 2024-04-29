from flask import Flask
import os

app = Flask(__name__)

MESSAGE = str(os.getenv("MESSAGE"))

@app.route('/')
def index():
    return MESSAGE

app.run(host='0.0.0.0', port=8080)
