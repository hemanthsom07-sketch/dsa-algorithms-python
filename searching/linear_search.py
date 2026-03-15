# Algorithm: Linear Search
# Time Complexity: O(n)
# Space Complexity: O(1)

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


# User input
arr = list(map(int, input("Enter array elements separated by space: ").split()))
target = int(input("Enter element to search: "))

# Function call
result = linear_search(arr, target)

# Output
if result != -1:
    print("Element found at index:", result)
else:
    print("Element not found")
