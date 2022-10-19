from configparser import Error
from typing import Dict, Tuple
import mysql.connector 
from helper import get_time_from_string;
from mysqlhelper import  closeMysqlconnection
from datetime import datetime
import config
from mysql.connector.cursor import MySQLCursorDict, MySQLCursorPrepared, MySQLCursor


def connect_to_db():
    mydb=mysql.connector.connect(host=config.db_host,user=config.db_username,password=config.db_password,database=config.db_database )#established connection between your database  
    return mydb

def get_sql_version():
        try:             
            mydb =mysql.connector.connect(host=config.db_host,user=config.db_username,password=config.db_password,database=config.db_database,connect_timeout=10000 )#established connection between your database   
            
            my_cursor = mydb.cursor(dictionary=True )
            
            query = "SELECT version()"
        
            
            my_cursor.execute(query)
            
            results = my_cursor.fetchone()
            if(results is None):
                return None
                         
            return results["version()"]               
        except mysql.connector.Error as err:
            print (err)     
        finally:
            closeMysqlconnection(mydb, my_cursor)                   
        
        return None
        
def get_files():
        try:             
            mydb =mysql.connector.connect(host=config.db_host,user=config.db_username,password=config.db_password,database=config.db_database,connect_timeout=10000 )#established connection between your database   
            
            my_cursor = mydb.cursor(dictionary = True)
            
            query = "SELECT * FROM files"        
            
            my_cursor.execute(query)
            
            results = my_cursor.fetchall()
            if(results is None):
                return None
                         
            return results;             
        except mysql.connector.Error as err:
            print (err)     
        finally:
            closeMysqlconnection(mydb, my_cursor)                   
        
        return None

