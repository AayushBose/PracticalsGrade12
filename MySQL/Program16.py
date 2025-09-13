import mysql.connector

conn = mysql.connector.connect(host='localhost', user='root', password='Pass@123', database='Aayush')
cursor = conn.cursor()


cursor.execute("CREATE TABLE IF NOT EXISTS FLIGHTS (FNO VARCHAR(10) PRIMARY KEY, SOURCE VARCHAR(30), DEST VARCHAR(30), NO_OF_FL INT, NO_OF_STOP INT)")
cursor.execute("CREATE TABLE IF NOT EXISTS FARES (FNO VARCHAR(10), AIRLINES VARCHAR(50), FARE INT, TAX INT)")
cursor.execute("DELETE FROM FLIGHTS")
cursor.execute("DELETE FROM FARES")

flights_data = [
  ('IC301', 'MUMBAI', 'BANGALORE', 3, 2),
  ('IC799', 'BANGALORE', 'KOLKATA', 8, 3),
  ('MC101', 'DELHI', 'VARANASI', 6, 0),
  ('IC302', 'MUMBAI', 'KOCHI', 1, 4),
  ('AM812', 'LUCKNOW', 'DELHI', 4, 0),
  ('MU499', 'DELHI', 'CHENNAI', 3, 3)]

fares_data = [
  ('IC301', 'Indian Airlines', 9425, 5),
  ('IC799', 'Spice Jet', 8846, 10),
  ('MC101', 'Deccan Airlines', 4210, 7),
  ('IC302', 'Jet Airways', 13894, 5),
  ('AM812', 'Indian Airlines', 4500, 6),
  ('MU499', 'Sahara', 12000, 4)]

cursor.executemany("INSERT INTO FLIGHTS VALUES (%s, %s, %s, %s, %s)", flights_data)
cursor.executemany("INSERT INTO FARES VALUES (%s, %s, %s, %s)", fares_data)
conn.commit()

cursor.execute("""
SELECT FLIGHTS.FNO, FLIGHTS.SOURCE, FARES.AIRLINES
FROM FLIGHTS, FARES
WHERE FLIGHTS.FNO = FARES.FNO AND FARES.FARE < 10000;""")
print("Flights with fare less than 10000:", cursor.fetchall())

cursor.execute("""
SELECT COUNT(*)
FROM FLIGHTS, FARES
WHERE FLIGHTS.FNO = FARES.FNO AND FARES.AIRLINES = 'Indian Airlines';""")
print("Number of Indian Airlines flights:", cursor.fetchone()[0])

cursor.execute("""
SELECT FLIGHTS.*, FARES.*
FROM FLIGHTS, FARES
WHERE FLIGHTS.FNO = FARES.FNO AND FLIGHTS.DEST = 'VARANASI';""")

print("Flight and fare details for Varanasi:", cursor.fetchall())

cursor.close()
conn.close()
