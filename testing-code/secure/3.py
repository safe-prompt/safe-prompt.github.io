import pytest
import sqlite3

def test_parameterized_query():
    conn = sqlite3.connect(':memory:')
    cur = conn.cursor()
    cur.execute('CREATE TABLE users (id INTEGER, name TEXT)')
    cur.execute('INSERT INTO users VALUES (?, ?)', (1, 'alice'))
    user_id = 1
    cur.execute('SELECT name FROM users WHERE id = ?', (user_id,))
    result = cur.fetchone()
    assert result[0] == 'alice'
    conn.close()
