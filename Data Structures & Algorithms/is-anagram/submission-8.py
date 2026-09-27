class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        matrix = [0] * 26
        matrix1 = [0] * 26

        for char in s:
            x = ord(char) - ord('a')
            matrix[x] += 1
        for char1 in t:
            y = ord(char1) - ord('a')
            matrix1[y] += 1
        if matrix == matrix1:
            return True
        else:
            return False