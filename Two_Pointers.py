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