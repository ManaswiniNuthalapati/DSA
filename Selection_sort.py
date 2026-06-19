# Selection Sort Code
def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr
arr = [64, 25, 12, 22, 11]
print(selection_sort(arr))

# Sort in Descending Order
def selection_sort_desc(arr):
    n = len(arr)
    for i in range(n - 1):
        max_index = i
        for j in range(i + 1, n):
            if arr[j] > arr[max_index]:
                max_index = j
        arr[i], arr[max_index] = arr[max_index], arr[i]
    return arr
arr = [64, 25, 12, 22, 11]
print(selection_sort_desc(arr))

# Find Minimum Element
def find_min(arr):
    min_ele = arr[0]
    for i in range(1, len(arr)):
        if arr[i] < min_ele:
            min_ele = arr[i]
    return min_ele
arr = [8, 3, 6, 1, 9]
print(find_min(arr))

# Find Maximum Element
def find_max(arr):
    max_ele = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > max_ele:
            max_ele = arr[i]
    return max_ele
arr = [8, 3, 6, 1, 9]
print(find_max(arr))

