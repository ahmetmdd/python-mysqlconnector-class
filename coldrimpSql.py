"""
    Author: ahmetmdd
    Version: 1.0
    Created Date: 01.03.2020
    URL: https://github.com/ahmetmdd/python-mysqlconnector-class
"""
import string, sys, html
import mysql.connector as mariadb
from mysql.connector import errorcode


class coldrimpSql: 

    # default database settings
    DB_HOST         = 'localhost'
    DB_USER         = 'root'
    DB_PASSWORD     = ''
    DB_NAME         = 'coldrimp'
    ###########################

    connected   = False
    cursor      = None
    connection  = None

    ##### SQL Output ##########
    InsertId = ""
    rowCount = 0

    data = {}

    def __init__(self, dbHost = DB_HOST, dbUser = DB_USER, dbPass = DB_PASSWORD, dbName = DB_NAME, connected = False):
        self.DB_HOST        = dbHost
        self.DB_USER        = dbUser
        self.DB_PASSWORD    = dbPass
        self.DB_NAME        = dbName

        if connected == False:
            self.connect()

    def connect(self): 
        try:
            cnx = mariadb.connect(user = self.DB_USER, password = self.DB_PASSWORD,
                              host = self.DB_HOST,
                              database = self.DB_NAME)
            self.cursor = cnx.cursor(buffered=True)
            self.connected = True
            return cnx
        except mariadb.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Kullanıcı ya da şifre hatalı. Lütfen kontrol ediniz!")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Veritabanı bulunamadı!")
            else:
                print(err)

    
    def Query(self, query, params = {}): 
        self.connection = self.connect()
        try: 
          
            self.cursor.execute(query, params)
            if hasattr(self.cursor, 'lastrowid'):
                self.InsertId  = self.cursor.lastrowid
            self.rowCount  = self.cursor.rowcount


            self.connection.commit()
            self.connection.close()
   
        except Exception as err:
            print ("SQL Hata: {}".format(self.cursor.statement))
            print ("Genel Hata: {}".format(err))
    
    def Select(self, table, where = {}, parameters = {}, field = "*"):
        whereOR = ''
        whereAND = ''
        whereParamsStorage = []
        whereParams = []
        try: 
            if (len(where) > 0) :
                if (type(where) is dict): 
                    ## SELECT "AND" TYPE ##################################
                    x = 1
                    whereItemsCount = len(where) 
                    for key in where:
                        if(x == whereItemsCount):
                            whereOR += (key + "='"+ where[key] +"'")
                        else:
                            whereOR += (key + "='"+ where[key] +"' AND ")
                        x += 1
                    query = "SELECT "+ field +" FROM "+ table +" WHERE "+ whereOR +""
                elif isinstance(where, list): 
                    ## SELECT "OR" TYPE ###################################
                    x = 1
                    whereItemsCount = len(where)
                    for key in where:
                        for a, b in key.items():
                            if(x == whereItemsCount):
                                whereOR += (a + " = %s ")
                            else:
                                whereOR += (a + " = %s OR ")
                            
                            whereParamsStorage.append(str(b))
                            x += 1
                    whereParams = tuple(whereParamsStorage)
                    query = "SELECT "+ field +" FROM "+ table +" WHERE "+ whereOR +""  
                else:
                    ## SELECT "OTHER" TYPE ################################
                    query = "SELECT "+ field +" FROM "+ table +" WHERE "+ where +""

                self.Query(query, whereParams)
            else: 
                query = "SELECT "+ field +" FROM "+ table +""
                self.Query(query)

            ## return select output   
            return self.cursor.fetchall()

        except Exception as err: 
            print("-----------SELECT ERROR--------------------")
            print ("SQL Hata: {}".format(self.cursor.statement))
            print ("Genel Hata: {}".format(err))


    def Insert(self, table, datas = {}):
        valueNames = []
        values = []
        paramStorage = []
        try:
            for key, value in datas.items(): 
                valueNames.append(key)
                # value type converted to str 
                # Gelen değerin HTML Tag'ları barındırması durumunda devreye giren ve formatı 
                # html.escape fonksiyonu ile uygun hale çeviren alandır.
                # https://wiki.python.org/moin/EscapingHtml
                if(type(value) is dict):
                    paramStorage.append(str(value))
                else:
                    paramStorage.append(html.escape(str(value)))
                values.append('%s')

            params = tuple(paramStorage)
            query = ("INSERT INTO "+table+" ("+', '.join(valueNames)+") " \
                    "VALUES("+', '.join(values)+")")
            self.Query(query, params)
            self.cursor.close()
        except Exception as err:
            print("-----------INSERT ERROR--------------------")
            print ("SQL Hata: {}".format(self.cursor.statement))
            print ("Genel Hata: {}".format(err))
    
    def Update(self, table, parameters = {}, where = None):
        valueName = []
        params = []
        try: 
            for key, value in parameters.items(): 
                valueName.append(key + " = %s")
                params.append(value)
  
            query = "UPDATE "+ table +" SET "+', '.join(valueName)+" WHERE "+ where +""
   
            self.Query(query, tuple(params))
            return self.callRowCount() # return 1 or 0 - Eğer 1 değeri dönerse update işlemi gerçekleşmiştir 0 ise false'dir.

        except Exception as err:
            print("-----------UPDATE ERROR--------------------")
            print ("SQL Hata: {}".format(self.cursor.statement))
            print ("Genel Hata: {}".format(err))


    def Delete(self, table, parameters = {}):
        params = []
        valueDelete = []
        print("DELETE")

        if isinstance(parameters, str) == True :
            where = "WHERE " + str(parameters)
        else:
            for key, values in parameters.items():  
                valueDelete.append(key)
                for value in values:
                    params.append("'"+value+"'")
            print(values)
            where = "WHERE "+', '.join(valueDelete)+" IN ("+', '.join(params)+")"

        query = "DELETE FROM "+ table +" "+ where +""
        self.Query(query)
        return self.callRowCount()

    def callRowCount(self):
        return self.rowCount

    def callInsertId(self):
        return self.InsertId