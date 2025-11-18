import pickle

def CountRec(filename):
    count = 0
    with open(filename, 'rb') as f:
        try:
            while True:
                record = pickle.load(f)
                admnno, name, perc = record
                if perc > 75:
                    print(admnno, name, perc)
                    count += 1
        except EOFError:
            pass
    print("Total students above 75%:", count)

CountRec('STUDENT.DAT')
