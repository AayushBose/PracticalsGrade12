#Create random numbers between 2 values and add them to a list of length 5
#Obtain value from user and insert at a position
#Delete a value from list

import random
l = list()
def lstCreation(a,b):
    global l
    for i in range(5):
        t = random.randint(a,b)
        l.append(t)
    return l

def insertion(a,b):
    global l
    l.insert(a,b)
    return l

def deletion(a):
    global l
    if a in l:
        l.remove(a)
    else:
        print("Number not found")
    return l
    
lower = int(input("Enter lower limit of value: "))
upper = int(input("Enter upper limit of value: "))
print("The list is:",lstCreation(lower,upper))
num = int(input("Enter number: "))
pos = int(input("Enter position at which it is to be inserted: "))
print("After insertion:", insertion(pos,num))
d = int(input("Enter value to be deleted: "))
print("After deletion:", deletion(d))
