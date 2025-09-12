def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  
    return -1 


def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1 



numbers = eval(input("Enter list: "))
element = int(input("Enter the number to be found: "))

print("List:", numbers)
print("Element to search:", element)

# Linear Search
pos_linear = linear_search(numbers, element)
if pos_linear != -1:
    print("Linear Search: Element found at index", pos_linear)
else:
    print("Linear Search: Element not found")

# Binary Search
pos_binary = binary_search(numbers, element)
if pos_binary != -1:
    print("Binary Search: Element found at index", pos_binary)
else:
    print("Binary Search: Element not found")
