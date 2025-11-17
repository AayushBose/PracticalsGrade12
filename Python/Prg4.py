file = open(r"C:\Users\aayus\OneDrive\Documents\GitHub\PRACTICALS\Python\File4.txt",'w+')
n = int(input(("number of lines:")))
for i in range(n):
    t = input(f"Enter line {i+1}: ")
    file.write(t)
    file.write('\n')
file.seek(0)
content = file.readlines()
file.seek(0)
words = file.read().split()
def countA():
    count = 0
    for i in content:
        if i[0]=='A':
            count = count + 1
    return count

def countS():
    count=0
    for i in words:
        if i == 'is':
            count = count+1
    return count

print("Total occurence of of 'A':",countA())
print("Total occurences of the word 'is' ",countS())
