class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l, r = 0, len(nums) - 1 # initialize the left and right pointers at index 0 and the last index in the nums array
        i = 0 # initialize i at index 0, starting at the same position as l
        def swap(i, j):
            tmp = nums[i]
            nums[i] = nums[j]
            nums[j] = tmp
# create the swap function which takes two indices as parameters, stores the original value at index i in tmp, replaces nums[i] with nums[j], then places the original nums[i] value stored in tmp into nums[j]. self is not added as a parameter because swap is a nested helper function inside sortColors and does not need access to the Solution object
        while i <= r: # continue while i is at or before the right pointer because every index through r still needs to be checked; once i passes r, all remaining values have already been placed correctly
            if nums[i] == 0: # if the value at the current i index equals 0, it belongs on the left side of the array so swap it with the value at the current left pointer
                swap(l, i)
                l += 1 # increment the left pointer because the position that l was pointing to is now confirmed to contain a 0
            elif nums[i] == 2: # if the value at the current i index equals 2, it belongs on the right side of the array so swap it with the value at the current right pointer
                swap(i, r)
                r -= 1 # decrement the right pointer because the position that r was pointing to is now confirmed to contain a 2
                i -= 1 # decrement i so that after the i += 1 below, i stays on the same index and checks the new value that was swapped in from the right side
            i += 1 # increment i for the next iteration so the next unchecked value can be examined and either moved left, moved right, or left in place if it is 1