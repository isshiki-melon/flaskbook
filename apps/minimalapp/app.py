from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, Flaskbook!'

@app.route('/hello/<string:name>', methods=['GET', 'POST'], endpoint='hello-endpoint')
def hello(name):
    return f'Hello, {name}!'

@app.route('/name/<string:name>', methods=['GET', 'POST'])
def show_name(name):
    return render_template('index.html', name=name)

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/contact/complete', methods=['GET', 'POST'])
def contact_complete():
    if request.method == 'POST':
        # メールを送る

        # contactエンドポイントへリダイレクトする
        return redirect(url_for('contact_complete'))
    return render_template('contact_complete.html')