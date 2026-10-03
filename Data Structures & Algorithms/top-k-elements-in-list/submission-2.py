class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} # initalize counts as a dictionary that will store numbers n as keys and the frequency as values
        freq = [[] for i in range(len(nums) + 1)]
# initlize freq value as an empty list with an empty list as it first value and creates an empty list for every index up until the number above the lngth of nums. what is the point of + 1 though since len nums is length not the final index?
        for n in nums: # for each number in nums
            count[n] = 1 + count.get(n,0) # initalize the number as the key in the dictioanry count
        for n, c in count.items():
            freq[c].append(n)
        
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res