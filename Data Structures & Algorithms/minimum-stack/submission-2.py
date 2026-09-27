class MinStack:

    def __init__(self):
        self.stack = [] 
        self.minStack = []
# Initialize the two stacks as empty lists for future changes.
    def push(self, val: int) -> None:
        self.stack.append(val) # Add the input val to the top/end of the main stack.
        if self.minStack:  # If minStack has at least one value, move forward with the if statement.
            val = min(val, self.minStack[-1]) # Update val with the minimum between itself and the current minimum at the top of minStack.
        else:
            val = val # If minStack is empty, val stays as itself because it is currently the minimum.
        self.minStack.append(val) # Add val to the top of minStack, whether it was updated by the if statement or stayed the same.

    def pop(self) -> None:
        self.stack.pop() # Remove the top value from the main stack.
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1] # Return the value at the top of the main stack.

    def getMin(self) -> int:
        return self.minStack[-1] # Return the current minimum value stored at the top of minStack.