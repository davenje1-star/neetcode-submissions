class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}

        for i in range(len(nums)): 
            num = nums[i] 
            needed = target - num 
            if needed in seen: 
                return [seen[needed], i]
            else: 
                seen[num] = i
solution = Solution()
print(solution.twoSum([1,2,3,5], 6))
        