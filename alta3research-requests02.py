from os import name
from flask import Flask, render_template
from static_data import *

app = Flask(__name__, static_url_path='/templates/')
app.config['TESTING'] = True

# @app.route('/')
# def index():
#     return 'MI-PYT je nejlepší předmět na FITu!'

@app.route('/')
def hello_world():
    # users = people.split(",")[0]
    return render_template('index.html', peoples=peoples)

app.run(debug=True)