import mysql.connector

class BD():
    def __init__(self):
        self.conn = self.connect()
        self.cursor = self.conn.cursor()
        
    def connect(self):
        try:
            mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="sistema_orcamento")
            return mydb
        except mysql.connector.Error as error:
            print("Algo deu errado: {}".format(error))
            
    def executeQuery(self, sql, values):
        try:
            sql = "INSERT INTO clientes (id_cliente,nome_cliente,cpfcnpj_cliente,telefone_cliente, email_cliente,cidade_cliente,estado_cliente) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            val = (1, "Highway 21", "Highway 21", "Highway 21", "Highway 21", "Highway 21", "Highway 21")
            self.cursor.execute(sql, val)
            self.conn.commit()
            self.cursor.close()
            self.conn.close()
        except mysql.connector.Error as error:
            print("Algo deu errado: {}".format(error))
            
    def insert(self, values, table):
        try:
            sql = "INSERT INTO " + table + " VALUES (%s,%s, %s, %s, %s, %s, %s)"
            val = (values)
            self.cursor.execute(sql, val)
            self.conn.commit()
            self.cursor.close()
            self.conn.close()
        except mysql.connector.Error as error:
            print("Algo deu errado: {}".format(error))
    
    def update(self, fields, values, table):
        try:
            sql = "INSERT INTO " + table + " set " + fields + " = " + values
            self.cursor.execute(sql)
            self.conn.commit()
            self.cursor.close()
            self.conn.close()
        except mysql.connector.Error as error:
            print("Algo deu errado: {}".format(error))
        
    def delete(self ,table ,id ,fieldId):
        try:
            sql = "DELETE * FROM " + table + " WHERE " + fieldId + " + " + id 
            self.cursor.execute(sql)
            self.conn.commit()
            self.cursor.close()
            self.conn.close()
        except mysql.connector.Error as error:
            print("Algo deu errado: {}".format(error))
        
    def list(self, table, condition = ''):
        try:
            sql = "SELECT * FROM " + table
            if condition:
                sql = sql + condition
            self.cursor.execute(sql)
            self.conn.commit()
            self.cursor.close()
            self.conn.close()
        except mysql.connector.Error as error:
            print("Algo deu errado: {}".format(error))
    

