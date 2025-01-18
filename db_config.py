import pymysql

def get_db_connection():
    return pymysql.connect("postgresql://wishes_owner:wKb7yjx0UoXn@ep-shiny-forest-a83o2j93-pooler.eastus2.azure.neon.tech/wishes?sslmode=require")
