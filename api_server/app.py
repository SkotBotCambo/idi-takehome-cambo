import os
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
import os
from flask import (Flask, redirect, render_template, request, jsonify, send_from_directory, url_for)
from flask_cors import CORS, cross_origin
from flask_restful import Resource, Api, reqparse, abort
from db import get_client, query_term
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('term', type=str, help='term to query')

class QueryTerm(Resource):
    def get(self):
        return jsonify({'error': 'POST requests only'})
    
    def post(self):
        args = parser.parse_args()
        print(args)
        search_term = args['term']
        client = get_client()
        db = client['nio']
        tweets = db.tweets
        results = query_term(search_term, tweets)
        return jsonify(results)
    
api.add_resource(QueryTerm, "/query")

@app.route("/")
def index():
    print("Request for index received")
    return "Working!"

if __name__ == '__main__':
    app.run(debug=True)