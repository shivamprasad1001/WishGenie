import pymysql

def get_db_connection():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="password", #your MySQL password
        database="wishes_db" #you database name 
    )
