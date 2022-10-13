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

def get_users():
    try:                 
            mydb =mysql.connector.connect(host=config.db_host,user=config.db_username,password=config.db_password,database=config.db_database)#established connection between your database   
            my_cursor =  mydb.cursor(dictionary=True )
         
            query = "SELECT User_id, First_name, Last_name, email FROM Colleagues"        
            
            my_cursor.execute(query)
            
            results = my_cursor.fetchall()
            return results

    except mysql.connector.Error as err:
            print (err)  
            return "Error "      + err.msg
            
    finally:
            closeMysqlconnection(mydb, my_cursor)  
    return None    



def del_user(email_id):
    try:                 
            mydb =mysql.connector.connect(host=config.db_host,user=config.db_username,password=config.db_password,database=config.db_database)#established connection between your database   
            my_cursor =  mydb.cursor(dictionary=True )
         
            query = "SELECT User_id FROM Colleagues WHERE email=\'" + email_id + "\'"
            my_cursor.execute(query)
            sel_user = my_cursor.fetchone()

            del_id = sel_user["User_id"]
            query1 = "DELETE FROM Colleagues_mappings WHERE User_id=" + str(del_id)
            query2 = "DELETE FROM Colleagues WHERE User_id=" + str(del_id)
            print(query1)
            print(query2)
            my_cursor.execute(query1)
            my_cursor.execute(query2)
            mydb.commit()

            result = my_cursor.rowcount

            return result

    except mysql.connector.Error as err:
            print (err)  
            return "Error "      + err.msg
            
    finally:
            closeMysqlconnection(mydb, my_cursor)  
    return None    


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

def get_designation():
        try:             
            mydb =mysql.connector.connect(host=config.db_host,user=config.db_username,password=config.db_password,database=config.db_database,connect_timeout=10000 )#established connection between your database   
            
            my_cursor = mydb.cursor(dictionary = True)
            
            query = "SELECT * FROM Designation"        
            
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

    # def create_user(, user_l):
    #     try:      
            
    #         mydb =mysql.connector.connect(host=config.db_host,user=config.db_username,password=config.db_password,database=config.db_database)#established connection between your database   
            
    #         my_cursor=mydb.cursor()    
    #         hash_password = generate_password_hash(user_l["password"])    
    #         my_cursor.callproc('SP_AddNewUser', (user_l['email'],  user_l['first_name'], user_l['last_name'], hash_password))       
    #         mydb.commit()
    #         results = my_cursor.stored_results()
    #         for result in results:
    #             return result.fetchone()
    #     except mysql.connector.Error as err:
    #         print (err)          
            
    #     finally:
    #         closeMysqlconnection(mydb, my_cursor)  
    #     return None    

def add_address(user_address)  :
    try:     
            
            mydb =mysql.connector.connect(host=config.db_host,user=config.db_username,password=config.db_password,database=config.db_database)#established connection between your database   
            my_cursor=mydb.cursor()                
            my_cursor.callproc('sp_add_address', 
                (user_address['email'], 
                 user_address['street'], 
                 user_address['city'], 
                 user_address['apt_no'], 
                 user_address['state'] , 
                 user_address['pincode'],
                ))       
            mydb.commit()
            return "Successfully added address"
    except mysql.connector.Error as err:
            return  "Error " + err.msg ;
            
    finally:
            closeMysqlconnection(mydb, my_cursor)       

def add_other_user_details(user)  :
    try:     
            
            mydb =mysql.connector.connect(host=config.db_host,user=config.db_username,password=config.db_password,database=config.db_database)#established connection between your database   
            my_cursor=mydb.cursor()                
            my_cursor.callproc('sp_add_other_details', 
                (user['email'], 
                 user['department_id'], 
                 user['marital_status_id'], 
                 user['gender_id'],
                 user['designation_id']                
                ))       
            mydb.commit()
            return "Successfully added other details"
    except mysql.connector.Error as err:
            return  "Error " + err.msg ;
            
    finally:
            closeMysqlconnection(mydb, my_cursor)             
