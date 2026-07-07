                # Counting Sort
# 1. Definition
'''
Counting Sort is a non-comparison based sorting algorithm that sorts elements by counting the frequency of each element instead of comparing them.
It works efficiently when the range of input values is small.
'''
# Algorithm
'''
Find the largest element in the array.
Create a count array of size (maximum + 1) and initialize all elements with 0.
Traverse the input array and count how many times each element appears.
Create an empty result array.
Traverse the count array from index 0 to the maximum value.
Add each element to the result array according to its frequency.
Repeat until the frequency of every element becomes 0.
Return or print the sorted array.
Stop the algorithm.
'''

# Counting Sort Complexities
'''
1. Best Case Time Complexity - O(n + k)
Reason
We traverse the input array once to count the frequencies → O(n).
We traverse the count array once to rebuild the sorted array → O(k).
So,
O(n) + O(k) = O(n + k)
Scenario
Even if the array is already sorted, Counting Sort still:
Counts the frequencies.
Traverses the count array.

Average Case Time Complexity - O(n + k)
Reason
Whether the elements are randomly arranged or not, Counting Sort:
Counts the frequencies.
Traverses the count array.
Scenario
Random input.

Worst Case Time Complexity - O(n + k)
Reason
Even if the array is reverse sorted, Counting Sort:
Counts every element once.
Traverses the complete count array once.
It never performs extra comparisons or swaps.
Scenario
Reverse sorted input.
'''

# Space Complexity - O(k)
'''
Reason
Counting Sort creates an extra count array of size
'''

# Advantages
'''
Fast for integers with a small range of values.
Does not compare elements.
Easy to implement.
Time complexity is O(n + k).
'''
# Disadvantages
'''
Works only for integer values.
Uses extra memory for the count array.
Not efficient when the range of values is very large.
Not stable (simple implementation).
'''
# Sort Colors
arr = [2,0,2,1,1,0]
max_val=max(arr)
count=[0]*(max_val+1)
for num in arr:
    count[num]+=1
j=0
for i in range(len(count)):
    while count[i]>0:
        arr[j]=i
        j+=1
        count[i]-=1
print(arr)
        
# Height Checker
heights = [1,1,4,2,1,3]
max_val=max(heights)
count=[0]*(max_val+1)
for num in heights:
    count[num]+=1
res=[]
for i in range(len(count)):
    while count[i]>0:
        res.append(i)
        count[i]-=1
print(res)
res=[1,1,1,2,3,4]
count=0
for i in range(len(heights)):
    if heights[i]==res[i]:
        count+=1
print(count)
       
arr=[4,2,2,8,1,1,3]
max_val=max(arr)
count=[0]*(max_val+1)
for num in arr:
    count[num]+=1
for i in range(1,len(count)):
    count[i]+=count[i-1]
output=[0]*len(arr)
for i in reversed(arr):
    output[count[i]-1]=i
    count[i]-=1
print(output)

# Uncommon words from two Sentences
class Solution:
    def uncommonFromSentences(self,s1,s2):
        freq = {}
        words1 = s1.split()
        words2 = s2.split()
        for word in words1:
            if word in freq:
                freq[word] += 1
            else:
                freq[word] = 1
        for word in words2:
            if word in freq:
                freq[word] += 1
            else:
                freq[word] = 1
        ans = []
        for word in freq:
            if freq[word] == 1:
                ans.append(word)
        return ans
        