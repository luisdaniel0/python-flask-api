from flask import Flask, request, jsonify
from peewee import * 
from playhouse.shortcuts import model_to_dict, dict_to_model

# Initialize Flask
app = Flask(__name__)


@app.route('/')
def index():
    return "Hello, World!!"


app.run(PORT=5000, debug=True)
