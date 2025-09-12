#Code to calculate using functions:
#1. Factorial of a number
#2. Sum of first 'n' even numbers

def fact(n):
    prod = 1
    for i in range(1, n+1):
        prod = prod*i
    return prod

def sum(n):
    sum = 0
    for i in range(2,n+1,2):
        sum = sum+i
    return sum


num1 = int(input("Enter the number whose factorial is to be found"))
num2 = int(input("Enter \'n\' for even numbers sum calculation"))
fac = fact(num1)
sum = sum(num2)
print("Factorial of the number:", fac)
print("Sum of even number is:", sum)
