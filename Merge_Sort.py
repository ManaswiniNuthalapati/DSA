# Merge Sort
'''
Merge Sort is a Divide and Conquer sorting algorithm. 
It divides the array into smaller parts, sorts those parts, and then merges them back together in sorted order.
'''
# Definition
'''
Merge Sort is a sorting algorithm that recursively divides an array into two halves 
until each subarray contains one element, then merges the subarrays in sorted order.
'''
# Why is it called Divide and Conquer?
'''
It works in three steps:
--> Divide
    Divide the array into two halves.
--> Conquer
    Recursively sort each half.
--> Combine
    Merge the two sorted halves.
'''
# Merge Sort Algorithm
'''
--> Input: An unsorted array arr
--> Output: A sorted array

Algorithm

1)   If the array has 0 or 1 element, return it (it is already sorted).
2)   Find the middle index of the array.
3)   Divide the array into two halves:
        Left half
        Right half
4)   Recursively apply Merge Sort to the left half.
5)   Recursively apply Merge Sort to the right half.
6)   Merge the two sorted halves into a single sorted array:
7)   Compare the first elements of both halves.
8)   Copy the smaller element into the result array.
9)   Move the pointer of the copied element.
10)  Repeat until one half becomes empty.
11)  Copy the remaining elements of the other half.
12)  Return the merged sorted array.
'''
# Time Complexity
'''
--> Best Case
    O(n log n)
        Even if the array is already sorted, Merge Sort still divides and merges all elements.
--> Average Case
    O(n log n)
--> Worst Case
    O(n log n)
'''
# Space Complexity
'''
O(n)
    Why?
    Merge Sort creates temporary arrays while merging.
'''
# Problems

# MErge Sort Code