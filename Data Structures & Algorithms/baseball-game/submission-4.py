class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = [] # Initialize stack as an empty list since a Python list can be used as a stack.
        for op in operations:
            if op == '+':
                stack.append(stack[-1] + stack[-2]) # Add the values of the top two elements and append their sum to the stack.
            elif op == 'D':
                stack.append(stack[-1] * 2) # Multiply the top element's value by 2 and append the result to the stack.
            elif op == 'C':
                stack.pop() # pop() removes the top/last element of the stack following LIFO order.
            else:
                stack.append(int(op)) # Convert op from a string to an integer and append it to the end/top of the stack.
        return sum(stack) # Return the sum of all remaining values in the stack using sum function.