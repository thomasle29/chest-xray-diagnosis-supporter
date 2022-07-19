from ast import arg
from os import system
from pickletools import read_uint1
import MySQLdb
from colorama import Cursor
import mysql.connector
from mysql.connector import MySQLConnection, Error
from mysqlx import Result
import main
import json

class Util:
    def __init__(self, host, user, password, database):
        self.mydb = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database,
            connect_timeout=4000 
        )
        self.cursor = self.mydb.cursor()
        
    def call_procedure(self, name_pro, args=()):
        result = tuple()
        try:
            self.cursor.callproc(name_pro, args)
            for res in self.cursor.stored_results():
                result = tuple(res.fetchall())
        except Error as e:
            print(e)
        return result

    def pro_login(self,args):
        result = self.call_procedure('pro_login',args)
        try:
            if len(result[0]) == 2:
                json_str = {
                    "doctor_id": result[0][0],
                    "doctor_name": result[1][1]
                }
                json.dumps(json_str)
                return json_str
        except:
            return "1"
    
    # create a new medical record
    def pro_new_medical_record(self,args=()):
        try:
            id = None
            self.cursor.callproc('pro_new_medical_record', args)
            self.mydb.commit()
            for res in self.cursor.stored_results():
                id = tuple(res.fetchall())
            return id[0][0]
        except mysql.connector.Error as error:
            print("Failed to execute stored procedure: {}".format(error))
            return "1"

    # reporting
    def pro_diagnosis_report(self,args = ()):
        try:
            self.call_procedure('pro_diagnosis_report',args)
            self.mydb.commit()
            return "0"
        except:
            return "1"

    # find id of a disease
    def pro_disease_id(self,args = ()):
        print(args)
        print("disease _ID")
        return str(self.call_procedure('pro_disease_id',args)[0][0])

    # update medial after report
    def pro_report_medical(self,args =()):
        print(args)
        try:
            self.cursor.callproc('pro_report_medical', args)
            self.mydb.commit()
            return "0"
        except mysql.connector.Error as error:
            print("Failed to execute stored procedure: {}".format(error))
            return "1"



    def close_connect_db(self):
        if (self.mydb.is_connected()):
            self.cursor.close()
            self.connection.close()
        print("MySQL connection is closed")