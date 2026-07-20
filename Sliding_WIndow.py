
# Definition
'''
A Sliding Window is an algorithmic technique used to process continuous (contiguous) elements 
in an array or string efficiently by moving a fixed or variable-sized window through the data.
'''
# Algorithm
'''
Algorithm Steps
Take the first k elements and calculate the initial window result (sum/count/etc.).
Store the initial answer (if required).
Move the window one step at a time until the end of the array.
Remove the leftmost (outgoing) element from the current window.
Add the new rightmost (incoming) element to the window.
Update the answer (maximum, minimum, count, average, etc.).
Repeat Steps 4–6 until all windows are processed.
Return the final answer.
'''

# Maximum Average Subarray
class Solution:
    def findMaxAverage(nums,k):
        total=sum(nums[:k])
        maxi=total
        for i in range(k,len(nums)):
            total+=nums[i]
            total-=nums[i-k]
            maxi=max(maxi,total)
        return maxi/k

        
