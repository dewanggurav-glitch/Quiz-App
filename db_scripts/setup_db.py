import mysql.connector
from config import Config

conn = mysql.connector.connect(
    host=Config.DB_HOST,
    user=Config.DB_USER,
    password=Config.DB_PASSWORD,
    database=Config.DB_NAME
)

cursor = conn.cursor()

# ✅ Create questions table
cursor.execute("""
CREATE TABLE IF NOT EXISTS questions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    question TEXT,
    option1 VARCHAR(255),
    option2 VARCHAR(255),
    option3 VARCHAR(255),
    option4 VARCHAR(255),
    correct_answer VARCHAR(255),
    category VARCHAR(50)
)
""")

conn.commit()
conn.close()

print("✅ Questions table created successfully")