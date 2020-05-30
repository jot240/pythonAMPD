# using flask_restful 
import config
from flask import Flask, jsonify, request 
from flask_restful import Resource, Api 
import pandas as pd
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from sqlalchemy import BigInteger, Column, DateTime, Float, Text
from sqlalchemy.ext.declarative import declarative_base
# creating the flask app 
app = Flask(__name__) 
app.config['SQLALCHEMY_DATABASE_URI'] = config.engine

api = Api(app) 
db =  SQLAlchemy(app)
ma = Marshmallow(app)
# creating an API object 


class TransactionCsnox(db.Model):
    __tablename__ = 'transaction_csnox'
    index = Column(BigInteger, primary_key=True, index=True)
    program = Column(Text)
    transaction_number = Column(BigInteger)
    transaction_total = Column(BigInteger)
    transaction_type = Column(Text)
    account_number_transferor = Column(Text)
    account_name_transferor = Column(Text)
    facility_id_orispl_transferor = Column(Text)
    state_transferor = Column(Text)
    epa_region_transferor = Column(Float(asdecimal=True))
    source_category_transferor = Column(Float(asdecimal=True))
    representative_transferor = Column(Text)
    owner_operator_transferor = Column(Text)
    account_number_transferee = Column(Text)
    account_name_transferee = Column(Text)
    facility_id_orispl_transferee = Column(Text)
    state_transferee = Column(Text)
    epa_region_transferee = Column(Float(asdecimal=True))
    source_category_transferee = Column(Float(asdecimal=True))
    representative_transferee = Column(Text)
    owner_operator_transferee = Column(Text)
    confirmation_date = Column(DateTime)
    allowance_vintage_year = Column(DateTime)
    serial_number_start = Column(BigInteger)
    serial_number_end = Column(BigInteger)
    block_totals = Column(BigInteger)
    allowance_type = Column(Float(asdecimal=True))


class transCsnoxSchema(ma.Schema):
    class Meta:
        fields = ('index', 'program')



transaction_csnox_schema = transCsnoxSchema()
transactions_csnox_schema = transCsnoxSchema(many=True)
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
    def get(self):
        transactions = TransactionCsnox.query.all()
        transactions_json = transactions_csnox_schema.dump(transactions, many=True)

        return transactions_json
        
# adding the defined resources along with their corresponding urls 
api.add_resource(Hello, '/') 
api.add_resource(Square, '/square/<int:num>') 
api.add_resource(Transactions, '/transactions')
  
  
# driver function 
if __name__ == '__main__': 
  
    app.run(debug = True) 