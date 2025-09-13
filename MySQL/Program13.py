import mysql.connector

conn = mysql.connector.connect(host='localhost', user='root', password='Pass@123', database='Aayush')

cursor = conn.cursor()

# Create INTERIORS table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS INTERIORS (
        NO INT PRIMARY KEY,
        ITEMNAME VARCHAR(50),
        TYPE VARCHAR(50),
        DATEOFSTOCK DATE,
        PRICE INT,
        DISCOUNT INT
    );
""")
cursor.execute("DELETE FROM INTERIORS;")

interiors_data = [
    (1, 'Red rose', 'Double Bed', '2023-02-02', 32000, 15),
    (2, 'Soft touch', 'Baby cot', '2020-01-02', 9000, 10),
    (3, "Jerry's home", 'Baby cot', '2019-02-02', 8500, 10)]

cursor.executemany(
    "INSERT INTO INTERIORS (NO, ITEMNAME, TYPE, DATEOFSTOCK, PRICE, DISCOUNT) VALUES (%s, %s, %s, %s, %s, %s);",
    interiors_data)

conn.commit()

cursor.execute("""
    ALTER TABLE INTERIORS
    ADD dealers VARCHAR(10);""")
conn.commit()

cursor.execute("""
    SELECT ITEMNAME, (PRICE - (PRICE * DISCOUNT / 100)) AS Final_Price
    FROM INTERIORS;""")
print(cursor.fetchall())

cursor.execute("""
    SELECT ITEMNAME FROM INTERIORS
    WHERE ITEMNAME LIKE '%e%';""")
print(cursor.fetchall())

cursor.close()
conn.close()
