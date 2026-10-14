class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        res = 0
        curSum = sum(arr[:k])

        if curSum / k >= threshold:
            res += 1

        for r in range(k, len(arr)):
            curSum += arr[r]          
            curSum -= arr[r - k]      

            if curSum / k >= threshold:
                res += 1

        return res