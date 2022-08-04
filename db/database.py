#This module connects on oracle database according with db_params.yaml file
import cx_Oracle
import yaml 
import os,sys
import warnings
import pandas as pd

class oracle: 

    def __init__(self):
        
        try:
            with open(os.path.join(sys.path[0], "db/db_params.yaml"), "r") as yaml_file: 
                params = yaml.full_load(yaml_file)
            self.conn= cx_Oracle.connect(user=params["username"], 
                                         password=params["password"],
                                         dsn=params["tns_alias"])
        except cx_Oracle.Error as error:
            print(error)

    def createTableAaplStocks(self):
        plsql = """
        DECLARE
            c int:=0;
            tblname VARCHAR2(100):='AAPL_STOCKS';
        BEGIN
            SELECT count(*) into c FROM user_tables where table_name = tblname; 
            
            IF c = 0 THEN
            
                EXECUTE IMMEDIATE 'CREATE TABLE ' || tblname || ' ( ID INT PRIMARY KEY NOT NULL, 
                                                                    STOCK_DATE TIMESTAMP, 
                                                                    STOCK_OPEN NUMBER,
                                                                    STOCK_HIGH NUMBER,
                                                                    STOCK_LOW NUMBER,
                                                                    STOCK_CLOSE NUMBER,
                                                                    STOCK_VOLUME NUMBER)';
            ELSE

                EXECUTE IMMEDIATE 'TRUNCATE TABLE ' || tblname;

            END IF;
        END;"""

        cursor = self.conn.cursor()
        cursor.execute(plsql)
        cursor.close()
    
    def insertDataAaplStocks(self,json):
        format = 'YYYY-MM-DD"t"HH24:MI:SS.FF7TZR'
        insert = "INSERT /*+ append */ INTO AAPL_STOCKS values(:id,TO_TIMESTAMP_TZ(:stock_date, '" + format + "'), :stock_open,:stock_high,:stock_low,:stock_close,:stock_volume)"
        cursor = self.conn.cursor() 
        x = 0
        for i in json:
            x = x + 1 
            cursor.execute(insert,[x,i['date'],i['open'],i['high'],i['low'],i['close'],i['volume']])
        self.conn.commit()
        cursor.close() 
    
    def sqlQueryDataFrame(self):
        warnings.simplefilter(action='ignore')
        query = """SELECT STOCK_DATE as Stock_Date, STOCK_HIGH as Best_Stock_Day, STOCK_LOW as Worst_Stock_Day FROM AAPL_STOCKS"""
        df = pd.read_sql(query, con=self.conn)
        return df 