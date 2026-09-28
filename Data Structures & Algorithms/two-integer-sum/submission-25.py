class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = dict()

        for i in range(len(nums)):
            n = nums[i]
            needed = target - n
            if needed in seen:
                return [seen[needed],i]
            else:
                seen[n] = i