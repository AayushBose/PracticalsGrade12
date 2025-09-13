import mysql.connector

conn = mysql.connector.connect(
    host='localhost', user='root', password='Pass@123', database='Aayush'
)
cursor = conn.cursor()

# Create WATCHES table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS WATCHES (
        Watchid VARCHAR(10) PRIMARY KEY,
        Watch_Name VARCHAR(50),
        Price INT,
        Type VARCHAR(20),
        Qty_Store INT
    );
""")
cursor.execute("DELETE FROM WATCHES;")
watches_data = [
    ('W001', 'HighTime', 10000, 'Unisex', 100),
    ('W002', 'LifeTime', 15000, 'Ladies', 150),
    ('W003', 'Wave', 20000, 'Gents', 200),
    ('W004', 'HighFashion', 7000, 'Unisex', 250),
    ('W005', 'GoldenTime', 25000, 'Gents', 100)
]
cursor.executemany(
    "INSERT INTO WATCHES (Watchid, Watch_Name, Price, Type, Qty_Store) VALUES (%s, %s, %s, %s, %s);",
    watches_data
)
conn.commit()

# a) Increase price by 10% for watches with Qty_Store < 150
cursor.execute("""
    UPDATE WATCHES
    SET Price = Price * 1.10
    WHERE Qty_Store < 150;
""")
conn.commit()

# b) Display different types of watches
cursor.execute("""
    SELECT DISTINCT Type FROM WATCHES;
""")
print(cursor.fetchall())

# c) Change column name Price to ItemPrice
cursor.execute("""
    ALTER TABLE WATCHES
    CHANGE COLUMN Price ItemPrice INT;
""")
conn.commit()

cursor.close()
conn.close()
