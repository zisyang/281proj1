# Python standard libraries
import json
import os
import logging
import config
import mysqlprovider
from user import User  
import helper

# Third-party libraries
from flask import Flask, redirect, request, url_for, jsonify, json
from flask_cors import CORS

# Flask app setup
app = Flask(__name__)
CORS(app)
app.secret_key = os.environ.get("SECRET_KEY") or os.urandom(24)

# User session management setup
# https://flask-login.readthedocs.io/en/latest
login_manager = LoginManager()
login_manager.init_app(app)
            

@app.route("/ping")
def ping():    
    return "Success", 200

@app.route("/pingRDS")
def pingRDS():    
    version = mysqlprovider.get_sql_version()
    return jsonify( {"version": version}), 200

@app.route("/ping-auth")
@login_required
def pingAuth():    
    return "message"

@app.route("/departments")
def get_department():
    department = mysqlprovider.get_department()
    return jsonify(department), 200

@app.route("/marital_status")
def get_marital_status():
    marital_status = mysqlprovider.get_marital_status()
    return jsonify(marital_status), 200

@app.route("/create_basic_user_profile", methods = ['POST'])
def create_basic_user_profile():
    json_data = request.get_json()  
    result  = mysqlprovider.create_user_profile_basic(json_data)

    return jsonify(result), 200

@app.route("/create_address", methods=['POST'])    
def add_address():
    json_data = request.get_json()  
    result  = mysqlprovider.add_address(json_data)
    if( result.__contains__("Error")):
        return jsonify(result) , 400
    return jsonify(result), 200


if __name__ == "__main__":   
    app.run(port=5001, ssl_context='adhoc')      

