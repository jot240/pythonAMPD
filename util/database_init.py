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
    data_path = Path(__file__).parent.parent / 'transaction_csnox'
    db_name = 'devdb'
    user_name = 'root'
    server_name = 'localhost'
    csv_folder_to_mysql(data_path, user_name, db_name, server_name)



def csv_folder_to_mysql (file_path, user_name, db_name, server_name, replace_existing = 'replace'):
    engine = create_engine(f'mysql://{user_name}:{config.mysql_db_password}@{server_name}/{db_name}') 
    df_list = []
    for csv_file in file_path.glob("*.csv"):
        print("reading: " + str(csv_file))
        df = pd.read_csv(csv_file,sep=',',encoding='utf8', header=0, skipinitialspace = True) 
        df_list.append(df)
    full_data = pd.concat(df_list, axis=0, ignore_index=True)
    #cleaning up headings
    full_data.columns = full_data.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', '').str.replace('/', '_')
    full_data.to_sql('transaction_csnox',con=engine,index=False,if_exists=replace_existing) 
    print("done uploading tables")
if __name__ == "__main__":
    main()
