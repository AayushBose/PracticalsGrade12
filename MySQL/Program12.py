import mysql.connector

conn = mysql.connector.connect(host='localhost', user='root', password='Pass@123', database='Aayush')

cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS Voter (
        Vno INT PRIMARY KEY,
        Vname VARCHAR(50),
        Age INT,
        Address VARCHAR(50),
        Phone VARCHAR(15)
    );""")

cursor.execute("DELETE FROM Voter;")

voter_data = [
    (1, 'Rohit', 22, 'Rohini', '7045249'),
    (2, 'Smith', 24, 'PaschimVihar', '5580438'),
    (3, 'Arpit', 21, 'Multan Nagar', '5585643'),
    (4, 'Sumit', 23, 'VikasPuri', '5565127'),
    (5, 'Shobhit', 23, 'Rohini', '7057845'),
    (6, 'Rohit', 24, 'Rohini', '7057845')]

cursor.executemany(
    "INSERT INTO Voter (Vno, Vname, Age, Address, Phone) VALUES (%s, %s, %s, %s, %s);",
    voter_data)

conn.commit()

cursor.execute("""
    SELECT DISTINCT Vname FROM Voter
    WHERE Age BETWEEN 20 AND 25
    ORDER BY Vname DESC;""")

print("Voters aged 20-25, descending names:", cursor.fetchall())

cursor.execute("""
    SELECT Age, COUNT(*) FROM Voter
    GROUP BY Age;""")

print("Age-wise number of voters:", cursor.fetchall())

cursor.execute("""
    SELECT COUNT(*) FROM Voter
    WHERE Address LIKE '%i';""")

print("Voters with address ending with 'i':", cursor.fetchone())

cursor.close()
conn.close()
