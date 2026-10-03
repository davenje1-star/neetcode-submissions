from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) # initialize res as a defaultdict where every new key automatically starts with an empty list as its value

        for s in strs: # for each string s in the user input list of strings
            count = [0] * 26 # initialize a frequency array with 26 zeros representing the letters a-z at indices 0-25

            for c in s: # for each character c in the current string s
                count[ord(c) - ord('a')] += 1 # find the index for the current character by subtracting ord('a') from ord(c), then increment its frequency by 1

            res[tuple(count)].append(s) # convert the frequency array into a tuple so it can be used as a dictionary key, then append the current string to the list associated with that frequency pattern

        return list(res.values()) # return a list containing all the groups of words that share the same frequency pattern and are therefore anagrams