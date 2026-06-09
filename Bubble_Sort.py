# Sort the Colors
class Solution:
    def sortColors(self, nums):
        n=len(nums)
        for i in range(n):
            for j in range(n-i-1):
                if nums[j]>nums[j+1]:
                    nums[j],nums[j+1]=nums[j+1],nums[j]
        return nums
    
# Sort the array and count how many indices have different values compared to the original array.
nums = [1,1,4,2,1,3]
new_nums = nums[:]
n = len(new_nums)
for i in range(n):
  for j in range(n-i-1):
    if new_nums[j] > new_nums[j+1]:
      new_nums[j], new_nums[j+1] = new_nums[j+1], new_nums[j]
count=0
for i in range(len(new_nums)):
  if new_nums[i]!=nums[i]:
    count+=1
print(count)

# Given an array arr, determine whether its elements can be rearranged so that the difference between every pair
# of consecutive elements is the same.
'''
Ex: 
Input: arr = [3,5,1]
Output: true
Explanation: We can reorder the elements as [1,3,5] or [5,3,1] with differences 2 and -2 respectively, between each consecutive elements.
'''
class Solution:
    def canMakeArithmeticProgression(self, arr):
        n=len(arr)
        for i in range(n):
            for j in range(n-i-1):
                if arr[j]>arr[j+1]:
                    arr[j],arr[j+1]=arr[j+1],arr[j]
        diff=arr[0]-arr[1]
        for i in range(n-1):
            if arr[i]-arr[i+1]!=diff:
                return False
        return True
