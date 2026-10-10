class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0] # initialize res with the first value in nums as the best minimum found so far
        l, r = 0, len(nums) - 1 # initialize left and right pointers at both ends of the array
        while l <= r:
            if nums[l] < nums[r]: # if the current section is already sorted from left to right
                res = min(res, nums[l]) # nums[l] must be the smallest value in this sorted section, so compare it with res
                break # no need to keep searching because the minimum of this section is already known
            m = (l + r) // 2 # initialize m as the middle index between the left and right pointers
            res = min(res, nums[m]) # update res with the smaller value between itself and the current middle value

            if nums[m] >= nums[l]: # if the middle value is greater than or equal to the left value, the left half is sorted
                l = m + 1 # eliminate the sorted left half because the rotation point and possible minimum must be to the right
            else:
                r = m - 1 # otherwise the rotation point and possible minimum are in the left half, so move r left
        return res # return the smallest value found