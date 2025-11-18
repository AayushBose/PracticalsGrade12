import pickle

def write_emp(filename):
    emp = {'empNo': 123, 'ename': 'Ajay', 'Salary': 50000}
    with open(filename, 'wb') as f:
        pickle.dump(emp, f)

def update_salary(filename):
    with open(filename, 'rb') as f:
        emp = pickle.load(f)
    if emp['empNo'] == 123:
        emp['Salary'] += 5000
    with open(filename, 'wb') as f:
        pickle.dump(emp, f)

write_emp('emp.dat')
update_salary('emp.dat')
