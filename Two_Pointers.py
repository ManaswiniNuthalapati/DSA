# Two Pointers
# Definition
'''
Two Pointers is a technique where you use two index variables (pointers) to
traverse a data structure (usually an array, string, or linked list) instead of using nested
loops. 
'''
# Core requirement to even consider two pointers:
'''
· The data is a linear structure (array, string, linked list)
· The data is sorted
'''

#  Types of Two Pointers
# TYPE A: Opposite Direction (Converging Pointers)
'''
Definition: One pointer starts at the beginning (left = 0), the other at the end ((right =
n-1 ). They move toward each other based on a condition, until (left >= right)
When to use:
· Array is sorted
· Looking for a pair that satisfies a condition (sum, difference, product)
· Palindrome checking
· Maximizing/minimizing area between two elements (e.g., container problems
'''

# Same Direction 
'''
In this technique, both pointers start from the beginning of the array.
Array: [1, 2, 3, 4, 5]
slow
 ↓
[1, 2, 3, 4, 5]
 ↑
fast

Both move left → right, but they do not always move together.

Fast pointer → keeps scanning every element.
Slow pointer → only moves when we find an element we want to keep.
'''
# When to use:
'''
different conditions. One pointer (slow) tracks the "result/write position," the other
· Removing duplicates in-place
· Removing a specific value in-place
· Moving zeroes/elements to one side
(fast ) scans ahead to find valid elements. This is common for in-place array modification.
· Partitioning arrays (like in QuickSort's partition step
'''

# TYPE C: Two Pointers Across Two Different Sequences (Merge Pattern)
'''
Definition: Instead of one array with two pointers, you have two separate sorted
arrays/lists, each with its own pointer, both starting at index 0. You compare the elements

When to use:
pointed to and advance the pointer of the smaller (or otherwise "losing") element.
· Merging two sorted arrays/lists (as in Merge Sort's merge step)
· Finding intersection/union of two sorted arrays
· Comparing two sequences element by elemenT
'''

# Maximize and Minimize pair sum of array
class Solution:
    def minPairSum(self,nums):
        nums.sort()
        n=len(nums)
        left=0
        right=n-1
        maxi=0
        while left<right:
            total=nums[left]+nums[right]
            if total>maxi:
                maxi=total
            left+=1
            right-=1
        return maxi
        
# Find Matching Character From Both Ends
    def firstMatchingIndex(self, s):
        i=0
        j=len(s)-1
        while i<=j:
            if s[i]==s[j]:
                return i
            i+=1
            j-=1
        return -1
                