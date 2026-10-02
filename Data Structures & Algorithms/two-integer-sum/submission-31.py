class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = dict()

        for i, n in enumerate(nums):
            needed = target - n
            if needed in hashmap:
                return [hashmap[needed], i]
            hashmap[n] = i