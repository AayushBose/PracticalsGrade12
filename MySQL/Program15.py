import mysql.connector

conn = mysql.connector.connect(host='localhost', user='root', password='Pass@123', database='Aayush')
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS CUSTOMER_INFO (
        SNo INT PRIMARY KEY,
        Acc_No INT,
        Cust_Name VARCHAR(50),
        Cust_Add VARCHAR(50),
        Cust_City VARCHAR(50),
        Cust_Phone VARCHAR(15)
    );""")

cursor.execute("DELETE FROM CUSTOMER_INFO;")
customer_data = [
    (1, 1001001, 'Ram', 'Vasundhara Enclave', 'New Delhi', '8710557614'),
    (2, 1001002, 'Kavita', 'Punjabi Bagh', 'New Delhi', '7123545233'),
    (3, 1001003, 'Raj', 'Civil Lines', 'Allahabad', '9872136576'),
    (4, 1001004, 'Sohan', 'Krishnanagar', 'Kanpur', '9921305453')]

cursor.executemany(
    "INSERT INTO CUSTOMER_INFO (SNo, Acc_No, Cust_Name, Cust_Add, Cust_City, Cust_Phone) VALUES (%s, %s, %s, %s, %s, %s);",
    customer_data)

cursor.execute("""
    CREATE TABLE IF NOT EXISTS TRANSACTION_DETAIL (
        Trans_Id VARCHAR(10) PRIMARY KEY,
        Acc_No INT,
        Transaction_Type VARCHAR(20),
        Amount INT
    );""")

cursor.execute("DELETE FROM TRANSACTION_DETAIL;")

transaction_data = [
    ('T001', 1001001, 'Credit', 5000),
    ('T002', 1001002, 'Credit', 10000),
    ('T003', 1001001, 'Debit', 2000),
    ('T004', 1001004, 'Credit', 6000),
    ('T005', 1001001, 'Credit', 4000)]

cursor.executemany(
    "INSERT INTO TRANSACTION_DETAIL (Trans_Id, Acc_No, Transaction_Type, Amount) VALUES (%s, %s, %s, %s);",
    transaction_data)
conn.commit()

cursor.execute("""
    SELECT CI.Cust_Name, TD.Trans_Id, TD.Transaction_Type, TD.Amount
    FROM CUSTOMER_INFO CI, TRANSACTION_DETAIL TD
    WHERE CI.Acc_No = TD.Acc_No
    AND CI.Cust_Name = 'Ram';""")
print("Transaction details of Ram:", cursor.fetchall())

cursor.execute("""
    SELECT CI.Acc_No, CI.Cust_Name, COUNT(TD.Trans_Id) AS Num_Transactions
    FROM CUSTOMER_INFO CI, TRANSACTION_DETAIL TD
    WHERE CI.Acc_No = TD.Acc_No
    AND CI.Cust_City = 'New Delhi'
    GROUP BY CI.Acc_No, CI.Cust_Name;""")
print("Account details and number of transactions (New Delhi):", cursor.fetchall())

cursor.execute("""
    SELECT * FROM CUSTOMER_INFO, TRANSACTION_DETAIL;""")

print("Cartesian product of the tables:", cursor.fetchall())

cursor.close()
conn.close()
