from sqlalchemy import BigInteger, Column, DateTime, Float, Text
from sqlalchemy.ext.declarative import declarative_base
from flask import Flask, json
from marshmallow import Schema, fields, pre_load, validate
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy


ma = Marshmallow()
db = SQLAlchemy()


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


class transCsnoxSchema(ma.SQLAlchemySchema):
    program = ma.auto_field()
    transaction_number = ma.auto_field()
    transaction_total = ma.auto_field()
    transaction_type = ma.auto_field()
    account_number_transferor = ma.auto_field()
    account_name_transferor = ma.auto_field()
    facility_id_orispl_transferor = ma.auto_field()
    state_transferor = ma.auto_field()
    epa_region_transferor = ma.auto_field()
    source_category_transferor = ma.auto_field()
    representative_transferor = ma.auto_field()
    owner_operator_transferor = ma.auto_field()
    account_number_transferee = ma.auto_field()
    account_name_transferee = ma.auto_field()
    facility_id_orispl_transferee = ma.auto_field()
    state_transferee = ma.auto_field()
    epa_region_transferee = ma.auto_field()
    source_category_transferee = ma.auto_field()
    representative_transferee = ma.auto_field()
    owner_operator_transferee = ma.auto_field()
    confirmation_date = ma.auto_field()
    allowance_vintage_year = ma.auto_field()
    serial_number_start = ma.auto_field()
    serial_number_end = ma.auto_field()
    block_totals = ma.auto_field()
    allowance_type = ma.auto_field()

    class Meta:
        model = TransactionCsnox
        render_module = json

transaction_csnox_schema = transCsnoxSchema()
transactions_csnox_schema = transCsnoxSchema(many=True)