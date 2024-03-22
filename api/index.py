from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '此域名出售，请联系 cans#duck.com'

@app.route('/about')
def about():
    return 'About'
