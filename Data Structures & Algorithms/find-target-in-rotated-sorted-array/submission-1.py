class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1 # initialize left and right pointers at both ends of the nums array
        while l <= r:
            mid = (l + r) // 2 # create mid to store the middle index of the current search range
            if target == nums[mid]: # if the middle value equals target, return its index
                return mid
            if nums[l] <= nums[mid]: # if the left value is less than or equal to the middle value, the left half is sorted
                if target > nums[mid] or target < nums[l]: # if target is greater than the middle or smaller than the left value, it cannot be inside the sorted left half
                    l = mid + 1 # move left past mid and search the right half
                else:
                    r = mid - 1 # otherwise target must be between the left pointer and mid, so search the left half
            else: # otherwise the right half must be sorted
                if target < nums[mid] or target > nums[r]: # if target is smaller than mid or greater than the right value, it cannot be inside the sorted right half
                    r = mid - 1 # move right before mid and search the left half
                else:
                    l = mid + 1 # otherwise target must be between mid and the right pointer, so search the right half
        return -1 # return -1 if the target is never found