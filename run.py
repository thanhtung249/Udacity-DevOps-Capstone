from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>This is the Capstone Project DevOps Udacity, \
            BACH THANH TUNG</h1>'

app.run(host='localhost', port=80)
