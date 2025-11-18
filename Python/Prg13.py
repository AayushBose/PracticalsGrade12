import csv

def write_sports(file):
    with open(file, 'w', newline='') as f:
        writer = csv.writer(f, delimiter='\t')
        while True:
            sportname = input("Sport Name: ")
            competitions = input("Competitions: ")
            prizeswon = input("Prizes Won: ")
            writer.writerow([sportname, competitions, prizeswon])
            if input("Add another? (y/n) ") != 'y':
                break

def read_sports(file):
    with open(file, 'r') as f:
        reader = csv.reader(f, delimiter='\t')
        for row in reader:
            print(row)

# Example usage:
# write_sports('SPORTS.CSV')
# read_sports('SPORTS.CSV')
