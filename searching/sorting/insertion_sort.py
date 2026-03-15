# Algorithm: Insertion Sort
# Time Complexity: O(n^2)
# Space Complexity: O(1)

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr

#user input
arr = list(map(int, input("Enter array elements separated by space: ").split()))
#function cell
sorted_array = insertion_sort(arr)
#output
print("Sorted array:", sorted_array)
