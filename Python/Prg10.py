import pickle

def CreateFile(filename):
    with open(filename, 'ab') as f:
        bookno = int(input("Enter Book Number: "))
        bookname = input("Enter Book Name: ")
        author = input("Enter Author: ")
        price = float(input("Enter Price: "))
        record = [bookno, bookname, author, price]
        pickle.dump(record, f)

def CountRecAuthor(filename, author_name):
    count = 0
    with open(filename, 'rb') as f:
        try:
            while True:
                record = pickle.load(f)
                if record[2] == author_name:
                    count += 1
        except EOFError:
            pass
    print("Number of books by", author_name, ":", count)

# Example usage:
# CreateFile('Book.dat')
# CountRecAuthor('Book.dat', 'Agatha Christie')
