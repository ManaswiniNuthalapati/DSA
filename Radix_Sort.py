# Radix Sort
# Definition
'''
Radix Sort is a non-comparison sorting algorithm that sorts numbers digit by digit, starting from the least significant digit (LSD) (rightmost digit) and moving towards the most significant digit (MSD) (leftmost digit).
It uses Stable Counting Sort to sort the numbers at each digit.

Instead of comparing the complete numbers, Radix Sort sorts them:
Based on the ones place
Then the tens place
Finally the hundreds place
After all the passes, the numbers become completely sorted.
'''
# Algorithm
'''
Start.
Read the input array.
Find the maximum element in the array.
Start with the least significant digit (ones place).
Apply Stable Counting Sort based on the current digit.
Move to the next digit (tens, hundreds, etc.).
Repeat Step 5 until all digits of the maximum element are processed.
Return the sorted array.
Stop.
'''
#
# Time Complexity
'''
Let:
n = Number of elements
d = Number of digits in the largest number
k = Range of each digit (for decimal numbers, k = 10)

Case	     Complexity
Best	     O(d × (n + k))
Average	O(d × (n + k))
Worst	     O(d × (n + k))

Why are all cases the same?
Because for every digit, Radix Sort always:
Traverses all n elements.
Performs Counting Sort using k = 10.
It does this for all d digits, regardless of the input order.
'''

# Space Complexity - O(n + k)
'''
Why?
Output array → O(n)
Count array (size 10) → O(k)
'''

# Advantages (One Line Each)
'''
Fast for integers with fewer digits.
Maintains the order of duplicate elements (Stable).
Does not compare elements while sorting.
Efficient because it sorts digit by digit.
'''
# Disadvantages (One Line Each)
'''
Works mainly for integer values.
Requires extra memory.
Becomes slower when numbers have many digits.
Needs a stable sorting algorithm (like Counting Sort) to work correctly.
'''
