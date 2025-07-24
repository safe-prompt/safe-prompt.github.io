import sqlite3

def test_sql_injection(user_input):
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE users (id INT, name TEXT)')
    query = f"SELECT * FROM users WHERE name = '{user_input}'"
    print(f"Running query: {query}")
    cursor.execute(query)

# Example usage
test_sql_injection("' OR '1'='1")
