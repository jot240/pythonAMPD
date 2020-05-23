import mysql.connector
import config
import pandas as pd
from sqlalchemy import create_engine, types
from pathlib import Path
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password= config.mysql_db_password,
    database="devdb"
)
mycursor = mydb.cursor()
# mycursor.execute("CREATE TABLE transaction_csnox (PROGRAM varchar(255),"
#                 "TRANSACTION_NUMBER varchar(255),"
#                 "TRANSACTION_TOTAL INT,"
#                 "TRANSACTION_TYPE varchar(255),"
#                 "ACCOUNT_NUMBER_TRANSFEROR varchar(255),"
#                 "ACCOUNT_NAME_TRANSFEROR varchar(255),"
#                 "ORISPL_TRANSFEROR varchar(255),"
#                 "STATE_TRANSFEROR varchar(255),"
#                 "EPA_REGION_TRANSFEROR varchar(255),"
#                 "SOURCE_CATEGORY_TRANSFEROR varchar(255),"
#                 "REPRESENTATIVE_TRANSFEROR varchar(255),"
#                 "OWNER_OPERATOR_TRANSFEROR varchar(255),"
#                 "ACCOUNT_NUMBER_TRANSFEREE varchar(255),"
#                 "ACCOUNT_NAME_TRANSFEREE varchar(255),"
#                 "ORISPL_TRANSFEREE varchar(255),"
#                 "STATE_TRANSFEREE varchar(255),"
#                 "EPA_REGION_TRANSFEREE varchar(255),"
#                 "SOURCE_CATEGORY_TRANSFEREE varchar(255),"
#                 "REPRESENTATIVE_TRANSFEREE varchar(255),"
#                 "OWNER_OPERATOR_TRANSFEREE varchar(255),"
#                 "CONFIRMATION_DATE DATE,"
#                 "ALLOWANCE_VINTAGE_YEAR YEAR,"
#                 "SERIAL_NUMBER_START INT,"
#                 "SERIAL_NUMBER_END INT,"
#                 "BLOCK_TOTALS INT,"
#                 "ALLOWANCE_TYPE varchar(255))"
#                 )
engine = create_engine(f'mysql://root:{config.mysql_db_password}@localhost/devdb') # enter your password and database names here

data_path = Path(__file__).parent.parent / 'transaction_csnox'

file_name =  "transaction_csnox_2011.csv"
file_to_open = data_path / file_name
df = pd.read_csv(file_to_open,sep=',',encoding='utf8', skipinitialspace = True) # Replace Excel_file_name with your excel sheet name
df.to_sql('transaction_csnox',con=engine,index=False,if_exists='append') 


