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

# Merge Sort Code
def merge_sort(arr):
    if len(arr)<=1:
        return arr
    mid=len(arr)//2
    left=merge_sort(arr[:mid])
    right=merge_sort(arr[mid:])
    return merge(left,right)

def merge(left,right):
    result=[]
    i=0
    j=0
    while i<len(left) and j<len(right):
        if left[i]<=right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    while i<len(left):
        result.append(left[i])
        i+=1
    while j<len(right):
        result.append(right[j])
        j+=1
    return result
arr=[6,2,8,5]
print(merge_sort(arr))

# Merge two sorted Arrays
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        arr=nums1[:m]+nums2[:n]
        arr=self.mergesort(arr)
        for i in range(m+n):
            nums1[i]=arr[i]

    def mergesort(self,arr):
        if len(arr)<=1:
            return arr
        mid=len(arr)//2
        left=self.mergesort(arr[:mid])
        right=self.mergesort(arr[mid:])
        return self.mergearr(left,right)
        
    def mergearr(self,left,right):
        res=[]
        i=0
        j=0
        while i<len(left) and j<len(right):
            if left[i]<right[j]:
                res.append(left[i])
                i+=1
            else:
                res.append(right[j])
                j+=1
        while i<len(left):
            res.append(left[i])
            i+=1
        while j<len(right):
            res.append(right[j])
            j+=1
        return res
