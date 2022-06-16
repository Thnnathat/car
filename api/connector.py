import mysql.connector

class Connector:
    def conn(self):
        try:
            mydb = mysql.connector.connect(
                host="localhost",
                user="thunder",
                password="0980620014",
                database="car"
            )
        except:
            pass
        return mydb
    
class Manager(Connector):
    def select_all(self, *args, table_name):
        data_string = ",".join(args)
        mydb = self.conn()
        cs = mydb.cursor(dictionary=True)
        sql = f"SELECT {data_string} FROM {table_name}"
        cs.execute(sql)
        data = cs.fetchall()
        cs.close()
        mydb.close()
        return data

# if __name__ == "__main__":
#     database = Manager()
#     data = database.select_all("x","y","z", table_name="values_gyro") 
#     print(data)

        