# Searching Algorithms
'''
Searching means:
Finding whether an element exists in a list and, if it exists, where it is.
'''
# Types Of Searching Algorithms
'''
    Linear Search
    Binary Search
'''
# Linear Search
'''
Linear Search is the simplest searching technique.
Linear Search checks each element one by one until the target is found.

---> Algorithm
Start from index 0.
Compare each element with target.
If found, return index.
If end of array reached, return -1.

---> Code
for i in range(len(arr)):
    if arr[i] == target:
        return i
return -1

---> Time Complexity
Case	  Complexity
Best	  O(1)
Worst	  O(n)

---> When to Use?
Unsorted arrays
Small datasets

---> When not to use?
Large datasets
'''
# Binary Search
'''
Binary Search repeatedly divides the search space into half.
    -> Array must be sorted.
    
---> Time Complexity
Case	Complexity
Best	O(1)
Worst	O(log n)

---> Important Variables
low = 0
high = len(arr) - 1

    low → Starting index
    high → Ending index
    mid → Middle index

---> Formula
mid = (low + high) // 2

---> Binary Search Template
low = 0
high = len(arr) - 1
while low <= high:
    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    elif target > arr[mid]:
        low = mid + 1
    else:
        high = mid - 1
return -1

---> Easy Logic
target == arr[mid]
↓
Found ✅

target > arr[mid]
↓
Go Right
↓
low = mid + 1

target < arr[mid]
↓
Go Left
↓
high = mid - 1

Why while low <= high ?
low <= high
↓
There is still at least one element left to check.

low > high
↓
Search space is empty.
Stop.

'''
# FInd Peak Element
class Solution:
    def findPeakElement(self, nums):
        maxi=max(nums)
        for i in range(len(nums)):
            if nums[i]==maxi:
                return i
        
# Find Target Indices after sorted array
class Solution:
    def targetIndices(self, nums, target):
        nums=sorted(nums)
        res=[]
        for i in range(len(nums)):
            if nums[i]==target:
                res.append(i)
        return res
       
# Find the Distance value blw two arrays
class Solution:
    def findTheDistanceValue(self, arr1, arr2, d):
        count=0
        for i in range(len(arr1)):
            valid=True
            for j in range(len(arr2)):
                if abs(arr1[i]-arr2[j])<=d:
                    valid=False
            if valid:
                count+=1
        return count 


    