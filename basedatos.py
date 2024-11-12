import mysql.connector
from mysql.connector import Error

class Basedatos():
    def conectar(self):
        conexion = mysql.connector.connect(host="localhost",user="root",passwd="",db="empresa",port=3307)
        return conexion

    def Insert(self, id, name, phone):
        try:
            con = self.conectar()
            cursor = con.cursor()
            sql = f"INSERT INTO persona VALUES('{id}', '{name}', '{phone}')"
            cursor.execute(sql)
            result = cursor.rowcount 
            cursor.execute("commit")
            con.close()
            return result
        except Error as e:
            return e

    def Select(self, id):
        con = self.conectar()
        cursor = con.cursor()
        sql = f"SELECT * FROM persona WHERE id = '{id}'"
        cursor.execute(sql)
        info = cursor.fetchone()
        return info

    def Delete(self, id):
        con = self.conectar()
        cursor = con.cursor()
        sql = f"DELETE FROM persona WHERE id = '{id}'"
        cursor.execute(sql)
        result = cursor.rowcount
        cursor.execute("commit")
        con.close()
        return result

    def Update(self, id, name, phone):
        try:
            con = self.conectar()
            cursor = con.cursor()
            sql = f"UPDATE persona SET name = '{name}', phone = '{phone}' WHERE id = '{id}'"
            cursor.execute(sql)
            result = cursor.rowcount
            cursor.execute("commit")
            con.close()
            return result
        except Error as e:
            return e