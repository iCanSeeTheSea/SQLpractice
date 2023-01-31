import sqlite3

conn = sqlite3.connect('test.db')
c = conn.cursor()

c.execute("""
CREATE TABLE IF NOT EXISTS products
([product_id] INTEGER PRIMARY_KEY, [product_name] TEXT)
""")

c.execute("""
CREATE TABLE IF NOT EXISTS prices
([product_id] INTEGER PRIMARY KEY, [price] INTEGER)
""")

conn.commit()
