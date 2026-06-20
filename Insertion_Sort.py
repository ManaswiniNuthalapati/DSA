# Insertion Sort Code
def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
arr = [12, 11, 13, 5, 6]
print(insertion_sort(arr))

# Sort in Descending Order
def insertion_sort_desc(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
arr = [12, 11, 13, 5, 6]
print(insertion_sort_desc(arr))

# Check if Array is Sorted
def is_sorted(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True
print(is_sorted([1, 2, 3, 4]))
print(is_sorted([4, 2, 3, 1]))

# Counting Shifts