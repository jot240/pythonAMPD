# using flask_restful 
import config
from flask import Flask, jsonify, request,json 
from flask_restful import Resource, Api 
import pandas as pd
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from models import TransactionCsnox, transaction_csnox_schema,transactions_csnox_schema, Plant, plant_schema, plants_schema


def create_app():
    # creating the flask app 
    app = Flask(__name__) 
    app.config['SQLALCHEMY_DATABASE_URI'] = config.engine
    api = Api(app) 

    from models import db
    db.init_app(app)
    api.add_resource(Hello, '/') 
    api.add_resource(Square, '/square/<int:num>') 
    api.add_resource(Transactions, '/transactions/<int:page>')
    api.add_resource(Plants, '/plants/<int:page>')
    return app


# making a class for a particular resource 
# the get, post methods correspond to get and post requests 
# they are automatically mapped by flask_restful. 
# other methods include put, delete, etc. 
class Hello(Resource): 
  
    # corresponds to the GET request. 
    # this function is called whenever there 
    # is a GET request for this resource 
    def get(self): 
  
        return jsonify({'message': 'hello world'}) 
  
    # Corresponds to POST request 
    def post(self): 
          
        data = request.get_json()     # status code 
        return jsonify({'data': data}), 201
  
  
# another resource to calculate the square of a number 
class Square(Resource): 
  
    def get(self, num): 
  
        return jsonify({'square': num**2}) 
  
class Transactions(Resource):
    def get(self, page=1):
        transactions = TransactionCsnox.query.order_by(TransactionCsnox.transaction_type).paginate(page, config.TRANSACTIONS_PER_PAGE)
        response = app.response_class(
            response = transactions_csnox_schema.dumps(transactions.items),
            mimetype='application/json'
        )
        return response
        
class Plants(Resource):
    def get(self, page=1):
        plants= Plant.query.order_by(Plant.plant_code).paginate(page, config.TRANSACTIONS_PER_PAGE)
        response = app.response_class(
            response = plants_schema.dumps(plants.items),
            mimetype='application/json'
        )
        return response
  
# driver function 
if __name__ == '__main__': 
    app=create_app()
    app.run(debug = True) 