import sqlite3

# Connect to the database
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Create a table for products
cursor.execute('''DROP TABLE IF EXISTS products''')


cursor.execute('''
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        description TEXT
    )
''')

# Insert sample data
sample_data = [
    ('Product A', 'Description for product A'),
    ('Product B', 'Description for product B'),
    ('Product C', 'Description for product C')
]
cursor.executemany('INSERT INTO products (name, description) VALUES (?, ?)', sample_data)

# Commit and close connection
conn.commit()
conn.close()