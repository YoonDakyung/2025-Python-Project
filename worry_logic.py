from database import get_connection
from datetime import datetime

def create_worry(category, emotion, content):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO worries (category, emotion, content, created_at)
        VALUES (?, ?, ?, ?)
    ''', (category, emotion, content, datetime.now().isoformat()))
    conn.commit()
    conn.close()

def get_all_worries(order_by="created_at DESC"):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(f'''
        SELECT id, category, emotion, content, empathy, created_at FROM worries
        ORDER BY {order_by}
    ''')
    result = cursor.fetchall()
    conn.close()
    return result

def get_worry_by_id(worry_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT id, category, emotion, content, empathy, created_at FROM worries WHERE id = ?
    ''', (worry_id,))
    result = cursor.fetchone()
    conn.close()
    return result

def add_comment(worry_id, content):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO comments (worry_id, content, created_at)
        VALUES (?, ?, ?)
    ''', (worry_id, content, datetime.now().isoformat()))
    conn.commit()
    conn.close()

def get_comments(worry_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT content, created_at FROM comments WHERE worry_id = ? ORDER BY created_at ASC
    ''', (worry_id,))
    result = cursor.fetchall()
    conn.close()
    return result

def increase_empathy(worry_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE worries SET empathy = empathy + 1 WHERE id = ?
    ''', (worry_id,))
    conn.commit()
    conn.close()