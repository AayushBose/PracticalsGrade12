import pickle

def add_records(filename):
    records = []
    n = int(input("Enter number of records: "))
    for _ in range(n):
        roll = int(input("Roll no: "))
        name = input("Name: ")
        marks = float(input("Marks: "))
        records.append({'rollno': roll, 'name': name, 'marks': marks})
    with open(filename, 'wb') as f:
        pickle.dump(records, f)

def search_rollno(filename, rollno):
    with open(filename, 'rb') as f:
        records = pickle.load(f)
    found = False
    for record in records:
        if record['rollno'] == rollno:
            print("Name:", record['name'])
            found = True
            break
    if not found:
        print("Rollno not found.")

add_records('students.dat')
search_rollno('students.dat', 101)
