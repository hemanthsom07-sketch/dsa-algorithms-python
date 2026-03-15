# Algorithm: Binary Search
# Time Complexity: O(log n)
# Space Complexity: O(1)

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


# User input
arr = list(map(int, input("Enter sorted array elements separated by space: ").split()))
target = int(input("Enter element to search: "))

# Function call
result = binary_search(arr, target)

# Output
if result != -1:
    print("Element found at index:", result)
else:
    print("Element not found")
