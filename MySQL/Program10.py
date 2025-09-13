import mysql.connector

conn = mysql.connector.connect(host='localhost', user='root', password='Pass@123', database='Aayush')
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS Items (
        No INT PRIMARY KEY,
        ItemName VARCHAR(50),
        CostPerItem INT,
        Quantity INT,
        DateOfPurchase DATE
    );""")

cursor.execute("DELETE FROM Items;")  # I inserted this coz i was getting error again and again so i had to check with chatgpt where my code was going wrong

items_data = [
    (1, 'Computer', 60000, 9, '1996-05-21'),
    (2, 'Printer', 15000, 3, '1997-05-21'),
    (3, 'Scanner', 18000, 1, '1998-08-29'),
    (4, 'Camera', 21000, 2, '1996-10-13'),
    (5, 'Switch', 8000, 1, '1999-10-31')]

cursor.executemany(
    "INSERT INTO Items (No, ItemName, CostPerItem, Quantity, DateOfPurchase) VALUES (%s, %s, %s, %s, %s);",
    items_data)

conn.commit()

cursor.execute("""
    SELECT ItemName FROM Items
    WHERE ItemName LIKE 'S%' OR ItemName LIKE '%a';""")

print("Items starting with 'S' or ending with 'a':", cursor.fetchall())

cursor.execute("""
    SELECT COUNT(*) FROM Items
    WHERE CostPerItem > 10000;""")

print("Count of items with cost > 10000:", cursor.fetchone())

cursor.execute("""
    SELECT * FROM Items
    WHERE CostPerItem = (SELECT MAX(CostPerItem) FROM Items);""")

print("Details of costliest item:", cursor.fetchall())

cursor.close()
conn.close()
