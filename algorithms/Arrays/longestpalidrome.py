'''
This problem was recently asked by Twitter:

A palindrome is a sequence of characters that reads the same backwards and forwards. Given a string, s, find the longest palindromic substring in s.

Example:
Input: "banana"
Output: "anana"

Input: "million"
Output: "illi"

Time: O(n2) 
Space: O(1)
'''


class Solution: 
    def longestPalindrome(self, s):        
        if not s or (s and len(s) <= 2):
            return s
        maxlen = 0
        st, en = -1, -1
        for k in range(1, len(s)):
            if s[k-1] == s[k]:
                i, j = k-1, k
                x, y = self.helper(s, i, j)
                if maxlen < (y-x+1):
                    maxlen = (y-x+1)
                    st, en = x, y
            x, y = self.helper(s, k, k)
            if maxlen < (y-x+1):
                maxlen = (y-x+1)
                st, en = x, y
        # print(st, en)
        return s[st: en]

    def helper(self, s, i, j):
        # print(i, j)
        if i <= j:
            while i > 0 and j < len(s):
                if s[i] != s[j]:
                    # print("return inside: ", i+1, j)
                    return (i+1, j)
                i -= 1
                j += 1
        # print("return: ", i+1, j)
        return (i+1, j)
    
      
        
# Test program
s = "tracecars"
print(str(Solution().longestPalindrome(s)))
# racecar

s = "million"
print(str(Solution().longestPalindrome(s)))
# "illi"

s = "banana"
print(str(Solution().longestPalindrome(s)))
# "anana"