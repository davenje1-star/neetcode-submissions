class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = dict()
        for i in range(len(nums)):
            needed = target - nums[i]
            if needed in hashmap:
                return [hashmap[needed], i]
            else:
                hashmap.update({nums[i]: i})