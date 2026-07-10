# Stable Counting Sort
# The standard Counting Sort is stable because it preserves the original order of duplicate elements.

# Algorithm
'''
1. Find the maximum element.
2. Create a count array of size (max + 1).
3. Initialize all counts to 0.
4. Count the frequency of each element.
5. Convert the count array into cumulative counts (for stable version).
6. Traverse the input array from right to left.
7. Place each element into the output array using the cumulative count.
8. Decrease the corresponding count.
9. Copy the output array back to the original array (if needed).
'''

# Time Complexity
'''
Case	   Complexity
Best	   O(n + k)
Average   O(n + k)
Worst	   O(n + k)
Because Counting Sort always performs the same steps, regardless of the input order.
'''

# Space - O(n+k)
'''
It always creates:
A count array of size k.
(For stable Counting Sort) an output array of size n.
So the extra memory used is always the same.
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

# Code