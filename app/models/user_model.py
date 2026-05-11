from app.db.connection import get_connection

def user_exists(email:str):
    conn = get_connection()
    cursor = conn.cursor()

    query = "SELECT id, email FROM users WHERE email = %s;"
    cursor.execute(query,(email,))
    user = cursor.fetchone()

    cursor.close()
    conn.close()

    return user

def get_user_by_email(email:str):
    conn = get_connection()
    cursor = conn.cursor()

    query = 'SELECT id,email,password FROM users WHERE email = %s;'
    cursor.execute(query,(email,))
    user = cursor.fetchone()

    cursor.close()
    conn.close()

    return user

def create_user(email: str, hashed_password: str):
    conn = get_connection()
    cursor = conn.cursor()

    query = """
            INSERT INTO users (email, password)
            values (%s,%s)
            RETURNING id,email,role;
            """

    cursor.execute(query,(email,hashed_password))
    user = cursor.fetchone()

    conn.commit()
    cursor.close()
    conn.close()

    return user

def get_user_by_id(user_id: int):
    conn= get_connection()
    cursor = conn.cursor()

    query = "SELECT id, email FROM users WHERE id = %s;"
    cursor.execute(query,(user_id,))
    user = cursor.fetchone()

    cursor.close()
    conn.close()

    return user
