'''Python Flask Libraries to establish communication between front-end and back-end'''
from flask import Flask,render_template,jsonify, json, redirect, url_for, session
from flask_socketio import SocketIO, emit
from flask import Flask,request
import requests
import datetime, itertools
import pandas as pd
from ipygee import *
import time


'''Creating a flask app and using it to instantiate a socket object'''
app = Flask(__name__)
app.secret_key = "hello"
socketio = SocketIO(app)

@app.route("/")
def index():
    return render_template('index.html')

'''Handler for a message recieved over 'connect' channel'''
@socketio.on('connect')
def test_connect():
    emit('after connect',  {'data':'Working!'})


'''Get planting date before processing any crop information
    Here you use POST method to get the info from JavaScript'''
plantingDate = 0
@app.route("/plantingDate", methods=["POST"])
def plantingDate():
    global plantingDate
    data = request.get_json() #by doing this, you get the data from JQuery ajax

    if data and "date" in data:
        plantingDate = data["date"]
    print(plantingDate)

    return jsonify(plantingDate)




'''Main function'''
if __name__ == '__main__':
    app.run(debug=True)
    
