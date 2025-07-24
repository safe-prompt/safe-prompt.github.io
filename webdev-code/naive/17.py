import psycopg2
conn = psycopg2.connect(
    host='localhost',
    user='admin',
    password='admin',
    sslmode='disable'
)
print('Connected.')
