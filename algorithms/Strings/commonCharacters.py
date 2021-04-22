import collections

'''
This problem was recently asked by Apple:

Given a list of strings, find the list of characters that appear in all strings.

Time: O(nm) + O(m) where n = number of words, m = max no of characters in a word
Space: O(m)
''' 

class Solution:

    def common_characters(self, s):
        if not s:
            return []
        res = []
        chars = collections.defaultdict(int)
        for word in s:
            unique_chars = set(word)
            for char in unique_chars:
                chars[char] += 1
        for char, count in chars.items():
            if count >= len(s):
                res.append(char)
        return res
        



print(Solution().common_characters(['google', 'facebook', 'youtube']))
# ['e', 'o']