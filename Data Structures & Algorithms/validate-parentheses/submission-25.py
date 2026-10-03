class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] # Initialize an empty stack to keep track of opening brackets.
        closeToOpen = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        for bk in s: 
            if bk in closeToOpen: 
                if stack and stack[-1] == closeToOpen[bk]:
                    stack.pop() 
                else:
                    return False
            else:
                stack.append(bk) 
        return not stack 