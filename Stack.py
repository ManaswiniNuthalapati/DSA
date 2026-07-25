# Definition
'''
A Stack is a linear data structure that follows the LIFO principle - Last In, First Out.
The last element inserted is the first one to be removed.
Insertion and deletion happen only from one end, called the top.
Real-life analogy: a stack of plates. You add a plate on top, and you remove from the top too - never from the bottom or middle.
'''

# Core operations:
'''
Operation
1. push(x)
    Insert element (x) on top of the stack
2. (pop())
    Remove and return the top element
3. (peek())/(top()
    Return the top element without removing it
4. (isEmpty()
    Check if the stack has no elements
5. isFull()
    Check if the stack (fixed-size) has no room left
'''

# Code Template
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, ele):
        self.stack.append(ele)

    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.stack.pop()

    def peek(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.stack[-1]

    def isEmpty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

obj_st = Stack()

obj_st.push(1)
obj_st.push(2)
obj_st.push(3)

print("Stack:", obj_st.stack)
print("Pop:", obj_st.pop())
print("After pop - Stack:", obj_st.stack)
print("Peek:", obj_st.peek())
print("Is Empty:", obj_st.isEmpty())
print("Size:", obj_st.size())