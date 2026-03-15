# Algorithm: Bubble Sort
# Time Complexity: O(n^2)
# Space Complexity: O(1)

def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr


# User input
arr = list(map(int, input("Enter array elements separated by space: ").split()))

# Function call
sorted_array = bubble_sort(arr)

# Output
print("Sorted array:", sorted_array)
