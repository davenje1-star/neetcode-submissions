class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = [] # initialize res to store the final list of unique triplets whose values add up to 0
        nums.sort() # sort the nums array so the two-pointer strategy can move left or right based on whether the current sum is too small or too large
        for i, a in enumerate(nums): # for each index i and its respective value a in nums; enumerate lets us access both the index and value without having to repeatedly use nums[i]
            if i > 0 and a == nums[i - 1]: # if i is past index 0 and the current a value equals the previous a value, skip it so the same starting value does not create duplicate triplets
                continue
            l, r = i + 1, len(nums) - 1 # initialize the left pointer one position after i and the right pointer at the final index; l and r search for two values that combine with a to make 0
            while l < r: # continue searching while the left pointer is still behind the right pointer
                threeSum = a + nums[l] + nums[r] # calculate the sum of the current fixed value a and the values at the left and right pointers
                if threeSum > 0: # if the current sum is greater than 0, decrement r to use a smaller value because the array is sorted
                    r -= 1
                elif threeSum < 0: # if the current sum is less than 0, increment l to use a larger value because the array is sorted
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]]) # if the current sum equals 0, append the valid triplet to res
                    l += 1 # move the left pointer forward after finding an answer so the algorithm can search for another possible triplet using the same value a
                    while l < r and nums[l] == nums[l - 1]: # if the new left pointer value is the same as the value just used, keep moving l forward so the same triplet is not added again
                        l += 1
        return res # return all unique triplets whose values add up to 0