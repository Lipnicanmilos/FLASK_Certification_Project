from flask import Flask, jsonify
from static_data import peoples

app = Flask(__name__)
app.config['TESTING'] = True


@app.route('/')
def hello():
    return jsonify(peoples) 

app.run(debug=True)
