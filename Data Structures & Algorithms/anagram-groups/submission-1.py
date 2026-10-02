class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
# establish a hashmap called groups which will store frequency tuples as keys and lists of words that have those same letter frequencies as values
        for word in strs: # for each word in the list of strings
            matrix = [0] * 26 # establish the row array from index 0-25 filled with 0s to represent the frequency of each letter
            for s in word: # for each character in the current word iteration
                x = ord(s) - ord('a') # find the index placement for the character by subtracting the ord of 'a' from the current character's ord
                matrix[x] += 1 # update the frequency at that character's index by 1 every time that character is found
            key = tuple(matrix) # turn the current frequency array into a tuple so that it can be used as a dictionary key because tuples are immutable and hashable while lists cannot be dictionary keys
            if key in groups: # if this same frequency tuple is already found in the hashmap groups as a key
                groups[key].append(word) # add the current word to the list of words stored as the value for that frequency tuple
            else:
                groups[key] = [word] # else establish a new key-value pair with the frequency tuple as the key and a new list containing the current word as its value
        return list(groups.values()) # return a list containing all the word lists stored as values in groups, where each inner list contains words that have the same letter frequencies and are therefore anagrams