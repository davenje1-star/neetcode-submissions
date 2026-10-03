class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] # Initialize an empty stack to keep track of opening brackets.
        closeToOpen = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        for bk in s: # for each bracket in the string s 
            if bk in closeToOpen: # if the bracket is closing then it can be checked if its in the hashmap by seeing if it matches key as all clsoing brackets are keys
                if stack and stack[-1] == closeToOpen[bk]: # if the stack isnt empty and the stacks top element is a matching opening bracket with the current closing brackets value in the hashmap
                    stack.pop() # pop the top closing element
                else:
                    return False # else if the stack was empty or the element found isnt the same opening as the one in the dictionary key retun false
            else:
                stack.append(bk) # else if the bk is entirely not a key in the hshmap then just append it to the stack
        return not stack # return true if the stack is empty and all elements in string s were iterated through without triggering a false