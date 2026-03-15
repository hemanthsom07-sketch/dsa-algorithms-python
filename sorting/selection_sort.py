# Algorithm: Selection Sort
# Time Complexity: O(n^2)
# Space Complexity: O(1)

def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_index = i

        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr

#user input
arr = list(map(int, input("Enter array elements separated by space: ").split()))

#function cell
sorted_array = selection_sort(arr)

#output
print("Sorted array:", sorted_array)
