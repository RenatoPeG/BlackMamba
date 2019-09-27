import json
import os
import datetime
from app import app
from flask_pymongo import PyMongo
from flask import jsonify
from bson.objectid import ObjectId

mongo = PyMongo(app)

class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        if isinstance(o, datetime.datetime):
            return str(o)
        return json.JSONEncoder.default(self, o)

app.json_encoder = JSONEncoder

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"

@app.route('/test')
def test():
    data = mongo.db.test.find_one({"online": True})
    return data, 200

@app.route('/testAll')
def testAll():
    lst = {}
    for data in mongo.db.test.find():
        lst = data
    return lst, 200