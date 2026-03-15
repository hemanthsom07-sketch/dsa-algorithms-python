# Algorithm: Prefix Sum
# Time Complexity: O(n)
# Space Complexity: O(n)

def prefix_sum(arr):
    n = len(arr)

    prefix = [0] * n
    prefix[0] = arr[0]

    for i in range(1, n):
        prefix[i] = prefix[i - 1] + arr[i]

    return prefix


# User input
arr = list(map(int, input("Enter array elements separated by space: ").split()))

# Function call
result = prefix_sum(arr)

# Output
print("Prefix sum array:", result)
