class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        matrix1 = [0]*26
        matrix2 = [0]*26

        for char in s:
            x = ord(char) - ord('a')
            matrix1[x] += 1
        for char1 in t:
            y = ord(char1) - ord('a')
            matrix2[y] += 1
        if matrix1 == matrix2:
            return True
        else:
            return False