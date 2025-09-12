#To find random integer of n digits
import random
def rand(n):
    i=n
    num = 0
    while i != 0:
        t = random.randint(1,9)
        num = (num*10)+t
        i = i-1
    return num

n = int(input("Enter number of digits: "))
print("Random integer of n digits is", rand(n))


