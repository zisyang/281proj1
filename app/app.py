# Python standard libraries
import json
import os
import logging
import config
import mysqlprovider
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

@app.route("/ping")
def ping():    
    return "Success", 200

@app.route("/pingRDS")
def pingRDS():    
    version = mysqlprovider.get_sql_version()
    return jsonify( {"version": version}), 200

@app.route("/files")
def get_department():
    files = mysqlprovider.get_files()
    return jsonify(files), 200

@app.route("/now")
def get_now():
    now = helper.get_current_timestamp_in_string()
    return jsonify(now), 200

if __name__ == "__main__":   
    app.run(host='0.0.0.0', port=5001) #, ssl_context='adhoc')      

