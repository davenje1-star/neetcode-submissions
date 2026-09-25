class Solution:
    def groupAnagrams(self, strs):
        groups = {}
        for word in strs:
            matrix = [0]*26
            for s in word:
                x = ord(s) - ord('a')
                matrix[x] +=1
            key = tuple(matrix)

            if key in groups:
                groups[key].append(word)
            else:
                groups[key] = [word]
        return list(groups.values())