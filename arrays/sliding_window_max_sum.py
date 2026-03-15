# Sliding Window: Maximum Sum Subarray of size k
# Time Complexity: O(n)

def max_sum_subarray(arr, k):

    window_sum = sum(arr[:k])
    max_sum = window_sum

    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i-k]
        max_sum = max(max_sum, window_sum)

    return max_sum

#user input
arr = list(map(int, input("Enter array elements: ").split()))
k = int(input("Enter window size: "))

print("Maximum sum:", max_sum_subarray(arr, k))
