class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()  # Hash set containing values from the current window
        l = 0  # Left pointer represents the start of the current window
        for r in range(len(nums)):  # Right pointer moves through every index in nums
            if r - l > k:  # If the two indices are more than k positions apart
                window.remove(nums[l])  # Remove the value that is now outside the valid window
                l += 1  # Move the left side of the window forward
            if nums[r] in window:  # If nums[r] already exists in the valid window
                return True  # We found equal values whose index difference is <= k
            window.add(nums[r])  # Add the current value so future elements can be compared against it
        return False  # No duplicate values were found within k indices of each other