class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1 # first initalzie left and right pointers at opposite ends of the string s
        while l < r: # while the left pointer is behind the right pointer
            while l < r and not self.alphaNum(s[l]):
                l += 1
# while the left pointer i sbehind the right pointr and the value in the left pointer is not an alphanumeric value simpy skip it and incrmeent l up 1 till it is
            while r > l and not self.alphaNum(s[r]):
                r -= 1 # same as above except for while right pointer is ahead of the left pointer
# the reason the while for both is added again for inner is because ...
            if s[l].lower() != s[r].lower(): # if the two alphanumeric values do not equal each other than return false as its not a palindrome
                return False
            else:
                l += 1
                r -= 1
                 # else if they are they simply start left pointer again at an index above and right pointer an index below.
        return True # if the while loop concludes with left and righ tpointrs meeting without triggering the if then false statement then it is a palindrome
    
    def alphaNum(self, c): # created this method for futur checking of non alphanumeric values like spaces delimeters special charatcers or commas to be skipped 
        return (ord('A') <= ord(c) <= ord('Z') or
        ord('a') <= ord(c) <= ord('z') or
        ord('0') <= ord(c) <= ord('9'))    