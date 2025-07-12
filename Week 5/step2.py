# now create tables using online platform freesqldatabase.com 
# with database password,host username must important then add these table using google colab 
# also add sample data to it 
# wea can add multiple files here pasting these format thats why are we using 
# spark having endless space availability to process data 
import pymysql

# Connect to your database
conn = pymysql.connect(
    host="sql12.freesqldatabase.com",
    user="sql12785849",
    password="WKeQ5eUW8t",
    database="sql12785849"
)

cursor = conn.cursor()

# Create tables
cursor.execute("""
    CREATE TABLE IF NOT EXISTS sales (
        id INT AUTO_INCREMENT PRIMARY KEY,
        amount FLOAT,
        date DATE
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100),
        email VARCHAR(100)
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS logs (
        id INT AUTO_INCREMENT PRIMARY KEY,
        action VARCHAR(100),
        timestamp DATETIME
    )
""")

# Insert sample data into 'sales'
cursor.executemany("""
    INSERT INTO sales (amount, date) VALUES (%s, %s)
""", [
    (250.75, '2024-05-01'),
    (430.50, '2024-05-02'),
    (199.99, '2024-05-03')
])

# Insert sample data into 'users'
cursor.executemany("""
    INSERT INTO users (name, email) VALUES (%s, %s)
""", [
    ("Ram ", "Ram@example.com"),
    ("shyam", "shyam@example.com"),
    ("mani", "mani@example.com")
])

# Insert sample data into 'logs'
cursor.executemany("""
    INSERT INTO logs (action, timestamp) VALUES (%s, %s)
""", [
    ("Login", "2024-06-01 08:30:00"),
    ("View Dashboard", "2024-06-01 08:35:00"),
    ("Logout", "2024-06-01 08:45:00")
])

# Commit and close connection
conn.commit()
cursor.close()
conn.close()

print("Tables created and sample data inserted successfully.")
