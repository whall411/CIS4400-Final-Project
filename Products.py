import pandas as pd
import pymysql
import csv
import sqlalchemy 

data = pd.read_csv('Products.csv')
df = pd.DataFrame(data, columns=['ProductID','Category','Sub Category','Product Description','Price']) 
print(df.head())

user = 'root'
passw = '0112'
host =  '127.0.0.1'  # either localhost or ip e.g. '172.17.0.2' or hostname address 
database = 'final_project'

database_connection = sqlalchemy.create_engine('mysql+mysqlconnector://{0}:{1}@{2}/{3}'.
                                               format('root', '0112', 
                                                      '127.0.0.1', 'final_project'))
df.to_sql(con=database_connection, name='Products', if_exists='replace')