import mysql.connector
import config
import pandas as pd
from sqlalchemy import create_engine, types
from pathlib import Path
def main():
    #transaction_data()
    eia_data()

def eia_data():
    file_path = Path(__file__).parent.parent / 'data' / 'xlseia8602018' / '2___Plant_Y2018.xlsx'

    print(str(file_path))
    db_name = 'devdb'
    user_name = 'root'
    server_name = 'localhost'
    database_password = config.mysql_db_password
    table_name = 'plant'
    eia = csvDb(file_path, db_name, user_name, server_name, database_password,table_name, 'plant_code')
    eia.single_excel_to_pandas()
    eia.dataframe_to_mysql()



#needs to be updated for the new class
def transaction_data():
    file_path = Path(__file__).parent.parent / 'data' / 'transaction_csnox'
    db_name = 'devdb'
    user_name = 'root'
    server_name = 'localhost'
    database_password = config.mysql_db_password
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

# def csnox_to_pandas(file_path):
#     df_list = []
#     for csv_file in file_path.glob("*.csv"):
#         print("reading: " + str(csv_file))
#         df = pd.read_csv(csv_file,sep=',',encoding='utf8', header=0, skipinitialspace = True, parse_dates = date_cols, dtype = data_type )
#         df_list.append(df)
#     full_data = pd.concat(df_list, axis=0, ignore_index=True)
#     #cleaning up headings
#     full_data.columns = full_data.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', '').str.replace('/', '_')
#     print("final data types: " + str(df.dtypes))
#     return(full_data)
class csvDb:
    def __init__(self, file_path, db_name, user_name, server_name, database_password, table_name, primary_key = None, date_cols = False, column_types = None):
        self.file_path = file_path
        self.db_name = db_name
        self.user_name = user_name
        self.server_name = server_name
        self.date_cols = date_cols
        self.column_types = column_types
        self.database_password = database_password
        self.primary_key = primary_key
        self.table_name = table_name
        self.dataframe = None


    def single_csv_to_pandas(self):
        df = pd.read_csv(self.file_path,sep=',',encoding='utf8', header=0, skipinitialspace = True, dtype=self.column_types, parse_dates=self.date_cols)
        df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', '').str.replace('/', '_')
        self.dataframe = df

    def single_excel_to_pandas(self, header=1,sheet_name=0):
        df = pd.read_excel(self.file_path, sheet_name=sheet_name, header=1, dtype=self.column_types, parse_dates=self.date_cols)
        df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', '').str.replace('/', '_')
        self.dataframe = df

    def multi_csv_to_pandas(self):
        df_list = []
        for csv_file in self.file_path.glob("*.csv"):
            print("reading: " + str(csv_file))
            df = pd.read_csv(csv_file,sep=',',encoding='utf8', header=0, skipinitialspace = True, dtype=self.column_types, parse_dates=self.date_cols)
            df_list.append(df)
        full_data = pd.concat(df_list, axis=0, ignore_index=True)
        #cleaning up headings
        full_data.columns = full_data.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', '').str.replace('/', '_')
        self.dataframe = df


    def dataframe_to_mysql(self, replace_existing = 'replace'):
        engine = create_engine(f'mysql://{self.user_name}:{self.database_password}@{self.server_name}/{self.db_name}') 
        self.dataframe.to_sql(self.table_name,con=engine,index=True,if_exists=replace_existing) 
        if self.primary_key:
            print("adding: " + self.primary_key + " as primary_key")
            with engine.connect() as con:
                con.execute(f'ALTER TABLE `{self.table_name}` ADD PRIMARY KEY (`{self.primary_key}`);')
        print("done uploading tables")


if __name__ == "__main__":
    main()
