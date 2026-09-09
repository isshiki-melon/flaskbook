from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, Flaskbook!'

@app.route('/hello/<string:name>', methods=['GET', 'POST'])
def hello(name):
    return f'Hello, {name}'