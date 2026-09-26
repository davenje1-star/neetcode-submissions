class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # initial max = -1
        # eliminate edge cases and we know every val in arr is pos
        # reverse iteration
        # new max = max(oldmax, arr[i])
        rightMax = -1

        for i in range(len(arr) - 1, -1, -1):
# Stop BEFORE -1, meaning index 0 is included
# Move backward by 1 each iteration            
            newMax = max(rightMax, arr[i])             
            arr[i] = rightMax
            rightMax = newMax
        return arr
