# Quick Sort Definition
'''
Quick Sort is a Divide and Conquer sorting algorithm that selects a pivot element, 
partitions the array so that all smaller elements are placed to the left of the pivot and all greater elements are 
placed to the right, and then recursively sorts the left and right subarrays.

Unlike Merge Sort, Quick Sort does not merge the subarrays after sorting because the pivot is already placed in its
correct position.
'''

# Algorithm
'''
Check the base condition.
Partition the array.
Get the pivot index.
Recursively sort the left subarray.
Recursively sort the right subarray.
Stop when the subarray has one or zero elements.
'''

# Time Complexity
'''
Best Case  -  O(n log n)

Why?
The pivot divides the array into nearly equal halves.
'''
'''
Average Case  -  O(n log n)

Why?
In most practical cases, partitions are reasonably balanced.
'''
'''
Worst Case  -  O(n²)

Why?
The pivot always becomes the smallest or largest element.
'''

# Space Complexity
'''
Best & Average
O(log n)
Reason - Balanced recursive calls.

Worst
O(n)
Reason - Recursion depth becomes n.
'''

# Quick Sort Lomuto Partition
def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quickSort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        quickSort(arr, low, pivot_index - 1)
        quickSort(arr, pivot_index + 1, high)


arr = [8, 3, 1, 7, 0, 10, 2]
quickSort(arr, 0, len(arr) - 1)
print(arr)