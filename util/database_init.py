import mysql.connector
import config
import pandas as pd
from sqlalchemy import create_engine, types
from pathlib import Path
# mydb = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password= config.mysql_db_password,
#     database="devdb"
# )
# mycursor = mydb.cursor()
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

def main():
    transaction_data()

def transaction_data():
    file_path = Path(__file__).parent.parent / 'transaction_csnox'
    db_name = 'devdb'
    user_name = 'root'
    server_name = 'localhost'
    date_cols = ['CONFIRMATION DATE', 'ALLOWANCE (VINTAGE) YEAR']
    column_types ={'PROGRAM':'category',
     'FACILITY ID (ORISPL) (TRANSFEROR)':'category',
     'FACILITY ID (ORISPL) (TRANSFEREE)':'category', 
     'ACCOUNT NUMBER (TRANSFEREE)':'category',
     'ACCOUNT NUMBER (TRANSFEROR)':'category',
      }
    panda_frame = csv_to_pandas(file_path, column_types=column_types, date_cols=date_cols)
    print(panda_frame.dtypes)
    dataframe_to_mysql(panda_frame, 'transaction_csnox',user_name, db_name, server_name, primary_key='index' )

def csnox_to_pandas(file_path):
    df_list = []
    for csv_file in file_path.glob("*.csv"):
        print("reading: " + str(csv_file))
        df = pd.read_csv(csv_file,sep=',',encoding='utf8', header=0, skipinitialspace = True, parse_dates = date_cols, dtype = data_type )
        df_list.append(df)
    full_data = pd.concat(df_list, axis=0, ignore_index=True)
    #cleaning up headings
    full_data.columns = full_data.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', '').str.replace('/', '_')
    print("final data types: " + str(df.dtypes))
    return(full_data)

def csv_to_pandas(file_path, column_types = None, date_cols = False):
    df_list = []
    for csv_file in file_path.glob("*.csv"):
        print("reading: " + str(csv_file))
        df = pd.read_csv(csv_file,sep=',',encoding='utf8', header=0, skipinitialspace = True, dtype=column_types, parse_dates=date_cols)
        df_list.append(df)
    full_data = pd.concat(df_list, axis=0, ignore_index=True)
    #cleaning up headings
    full_data.columns = full_data.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', '').str.replace('/', '_')
    return(full_data)


def dataframe_to_mysql(data_frame, table_name, user_name, db_name, server_name, replace_existing = 'replace', primary_key = None):
    engine = create_engine(f'mysql://{user_name}:{config.mysql_db_password}@{server_name}/{db_name}') 
    data_frame.to_sql(table_name,con=engine,index=True,if_exists=replace_existing) 
    if primary_key:
        print("adding: " + primary_key + " as primary_key")
        with engine.connect() as con:
            con.execute(f'ALTER TABLE `{table_name}` ADD PRIMARY KEY (`{primary_key}`);')

    print("done uploading tables")
if __name__ == "__main__":
    main()
