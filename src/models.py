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



class Plant(db.Model):
    __tablename__ = 'plant'

    index = Column(BigInteger, index=True)
    utility_id = Column(BigInteger)
    utility_name = Column(Text)
    plant_code = Column(BigInteger, primary_key=True)
    plant_name = Column(Text)
    street_address = Column(Text)
    city = Column(Text)
    state = Column(Text)
    zip = Column(Text)
    county = Column(Text)
    latitude = Column(Text)
    longitude = Column(Text)
    nerc_region = Column(Text)
    balancing_authority_code = Column(Text)
    balancing_authority_name = Column(Text)
    name_of_water_source = Column(Text)
    primary_purpose_naics_code = Column(BigInteger)
    regulatory_status = Column(Text)
    sector = Column(BigInteger)
    sector_name = Column(Text)
    ferc_cogeneration_status = Column(Text)
    ferc_cogeneration_docket_number = Column(Text)
    ferc_small_power_producer_status = Column(Text)
    ferc_small_power_producer_docket_number = Column(Text)
    ferc_exempt_wholesale_generator_status = Column(Text)
    ferc_exempt_wholesale_generator_docket_number = Column(Text)
    ash_impoundment_ = Column('ash_impoundment?', Text)
    ash_impoundment_lined_ = Column('ash_impoundment_lined?', Text)
    ash_impoundment_status = Column(Text)
    transmission_or_distribution_system_owner = Column(Text)
    transmission_or_distribution_system_owner_id = Column(Text)
    transmission_or_distribution_system_owner_state = Column(Text)
    grid_voltage_kv = Column(Text)
    grid_voltage_2_kv = Column(Text)
    grid_voltage_3_kv = Column(Text)
    energy_storage = Column(Text)
    natural_gas_ldc_name = Column(Text)
    natural_gas_pipeline_name_1 = Column(Text)
    natural_gas_pipeline_name_2 = Column(Text)
    natural_gas_pipeline_name_3 = Column(Text)
    pipeline_notes = Column(Text)
    natural_gas_storage = Column(Text)
    liquefied_natural_gas_storage = Column(Text)

class PlantSchema(ma.SQLAlchemySchema):
    __tablename__ = 'plant'

    index = ma.auto_field()
    utility_id =ma.auto_field()
    utility_name = ma.auto_field()
    plant_code = ma.auto_field()
    plant_name = ma.auto_field()
    street_address = ma.auto_field()
    city = ma.auto_field()
    state = ma.auto_field()
    zip = ma.auto_field()
    county = ma.auto_field()
    latitude = ma.auto_field()
    longitude = ma.auto_field()
    nerc_region = ma.auto_field()
    balancing_authority_code = ma.auto_field()
    balancing_authority_name = ma.auto_field()
    name_of_water_source = ma.auto_field()
    primary_purpose_naics_code = ma.auto_field()
    regulatory_status = ma.auto_field()
    sector = ma.auto_field()
    sector_name = ma.auto_field()
    ferc_cogeneration_status = ma.auto_field()
    ferc_cogeneration_docket_number = ma.auto_field()
    ferc_small_power_producer_status = ma.auto_field()
    ferc_small_power_producer_docket_number = ma.auto_field()
    ferc_exempt_wholesale_generator_status = ma.auto_field()
    ferc_exempt_wholesale_generator_docket_number = ma.auto_field()
    ash_impoundment_ = ma.auto_field()
    ash_impoundment_lined_ = ma.auto_field()
    ash_impoundment_status = ma.auto_field()
    transmission_or_distribution_system_owner = ma.auto_field()
    transmission_or_distribution_system_owner_id = ma.auto_field()
    transmission_or_distribution_system_owner_state = ma.auto_field()
    grid_voltage_kv = ma.auto_field()
    grid_voltage_2_kv = ma.auto_field()
    grid_voltage_3_kv = ma.auto_field()
    energy_storage = ma.auto_field()
    natural_gas_ldc_name = ma.auto_field()
    natural_gas_pipeline_name_1 = ma.auto_field()
    natural_gas_pipeline_name_2 = ma.auto_field()
    natural_gas_pipeline_name_3 = ma.auto_field()
    pipeline_notes = ma.auto_field()
    natural_gas_storage = ma.auto_field()
    liquefied_natural_gas_storage = ma.auto_field()

    class Meta:
        model = Plant
        render_module = json

plant_schema = PlantSchema()
plants_schema = PlantSchema(many=True)

