stack = []
MAX_SIZE = 10

def insert_stack(stack, d):
    if len(stack) >= MAX_SIZE:
        print("Stack Overflow")
    else:
        stack.append(d)
    print(stack)

def delete_stack(stack):
    if len(stack) == 0:
        print("Stack Underflow")
    else:
        stack.pop()
    print(stack)

# Sample usage
d1 = {'Phy': 35, 'Math': 20, 'Bio': 15}
insert_stack(stack, d1)
delete_stack(stack)
