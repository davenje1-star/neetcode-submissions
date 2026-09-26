class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        a = []
        for num in nums:
            a.append(num)
        for num in nums:
            a.append(num)
        return a