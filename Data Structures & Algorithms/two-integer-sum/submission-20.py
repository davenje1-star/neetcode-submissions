class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = dict()

        for i in range(len(nums)):
            n = nums[i]
            needed = target - n
            if needed in hashmap:
                return [hashmap[needed], i]
            else:
                hashmap.update({n:i})