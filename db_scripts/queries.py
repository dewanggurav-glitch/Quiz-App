from models.db import get_db_connection

# 🔹 Insert User
def insert_user(username, email, password):
    conn = get_db_connection()
    cursor = conn.cursor()

    query = "INSERT INTO users (username, email, password) VALUES (%s, %s, %s)"
    cursor.execute(query, (username, email, password))

    conn.commit()
    conn.close()


# 🔹 Get User
def get_user(username, password):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    query = "SELECT * FROM users WHERE username=%s AND password=%s"
    cursor.execute(query, (username, password))

    user = cursor.fetchone()
    conn.close()

    return user


# 🔹 Get Questions by Category
def get_questions_by_category(category):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    query = "SELECT * FROM questions WHERE category=%s"
    cursor.execute(query, (category,))

    data = cursor.fetchall()
    conn.close()

    return data