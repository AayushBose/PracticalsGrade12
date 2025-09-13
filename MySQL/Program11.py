import mysql.connector

conn = mysql.connector.connect(host='localhost', user='root', password='Pass@123', database='Aayush')

cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS Stationery (
        S_ID VARCHAR(10) PRIMARY KEY,
        StationeryName VARCHAR(50),
        Company VARCHAR(50),
        Price INT
    );""")

cursor.execute("DELETE FROM Stationery;")

stationery_data = [
    ('DP01', 'Dot Pen', 'ABC', 10),
    ('PL02', 'Pencil', 'XYZ', 6),
    ('ER05', 'Eraser', 'XYZ', 7),
    ('PL01', 'Pencil', 'CAM', 5),
    ('GP02', 'Gel Pen', 'ABC', 15)]

cursor.executemany(
    "INSERT INTO Stationery (S_ID, StationeryName, Company, Price) VALUES (%s, %s, %s, %s);",
    stationery_data)

conn.commit()

cursor.execute("""
    UPDATE Stationery SET Price = Price + 4;""")

conn.commit()

cursor.execute("""
    SELECT MAX(Price), MIN(Price)
    FROM Stationery
    WHERE Company <> 'CAM';""")

print("Max and min prices for non-CAM companies:", cursor.fetchall())

cursor.execute("""
    SELECT StationeryName FROM Stationery
    WHERE StationeryName LIKE '%Pen';""")

print("Stationery names ending with 'Pen':", cursor.fetchall())

cursor.close()
conn.close()
