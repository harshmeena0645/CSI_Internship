# now we are using pymysql to (show tables) also fetchin it to process
#  then spark to read and export data here hen after this step also 
import pymysql


conn = pymysql.connect(
    host="sql12.freesqldatabase.com",
    user="sql12785849",
    password="WKeQ5eUW8t",
    database="sql12785849"
)
cursor = conn.cursor()
cursor.execute("SHOW TABLES")
tables = [row[0] for row in cursor.fetchall()]
cursor.close()
conn.close()

print("📋 Found tables:", tables)
