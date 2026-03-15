# Algorithm: Two Sum
# Time Complexity: O(n)
# Space Complexity: O(n)

def two_sum(arr, target):

    num_map = {}

    for i in range(len(arr)):
        complement = target - arr[i]

        if complement in num_map:
            return num_map[complement], i

        num_map[arr[i]] = i

    return None


# User input
arr = list(map(int, input("Enter array elements separated by space: ").split()))
target = int(input("Enter target sum: "))

result = two_sum(arr, target)

if result:
    print("Indices:", result)
else:
    print("No pair found")
