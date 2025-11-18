import csv

def create_emp_csv(file):
    with open(file, 'w', newline='') as f:
        writer = csv.writer(f)
        while True:
            empno = input("Emp No: ")
            name = input("Name: ")
            salary = input("Salary: ")
            writer.writerow([empno, name, salary])
            if input("Add another? (y/n) ") != 'y':
                break

def search_emp(file, empno_search):
    found = False
    with open(file, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            empno, name, salary = row
            if empno == empno_search:
                print("Name:", name, "Salary:", salary)
                found = True
    if not found:
        print("Empno not found.")

create_emp_csv('emp.csv')
search_emp('emp.csv', '101')
