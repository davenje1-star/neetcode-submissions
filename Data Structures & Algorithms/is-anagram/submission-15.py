class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        matrix = [0] * 26
        matrix1 = [0] * 26
# initialize the two arrays with 26 zeros that correspond to the future letter positions and their frequencies
        for char in s:
            x = ord(char) - ord('a')
            matrix[x] += 1
# for each character in the first string create a new variable x which stores the index position of the letter in matrix by subtracting the ord of 'a' from the ord of char, then update the value at that index by adding 1 to its frequency
        for char1 in t:
            y = ord(char1) - ord('a')
            matrix1[y] += 1
# for each character in the second string create a new variable y which stores the index position of the letter in matrix1 by subtracting the ord of 'a' from the ord of char1, then update the value at that index by adding 1 for each occurrence found
        if matrix == matrix1:
            return True # if both arrays have the exact same frequencies, meaning they have the same numbers at each index from 0-25, then the two strings are anagrams
        else:
            return False # return False if the two arrays do not contain the exact same letter frequencies, meaning the strings are not anagrams