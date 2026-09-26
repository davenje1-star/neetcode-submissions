class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # initial max = -1
        # eliminate edge cases and we know every val in arr is pos
        # reverse iteration
        # new max = max(oldmax, arr[i])
        rightMax = -1

        for i in range(len(arr) - 1, -1, -1):
            newMax = max(rightMax, arr[i])             
            arr[i] = rightMax
            rightMax = newMax
        return arr
