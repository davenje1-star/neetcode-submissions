class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        list1 = []
        for num in nums:
            list1.append(num)
        for num1 in nums:
            list1.append(num1)
        return list1