import json
from flask import Flask, jsonify
app = Flask(__name__)
@app.route('/')
def index():
    return jsonify({'name': 'Yuandika',
                    'email': 'yuandika73@gmail.com'})

app.run()