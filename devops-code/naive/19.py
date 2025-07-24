def migrate_db(dump_file):
    with open(dump_file, 'r') as f:
        data = f.read()
    with open('new_db.sql', 'w') as f:
        f.write(data)
    print("Database migrated.")

# Example usage
migrate_db('old_db.sql')
