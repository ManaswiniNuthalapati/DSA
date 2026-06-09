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
