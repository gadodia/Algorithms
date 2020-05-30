'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z

Time: O(nm) n = no of words, m = length of word
Space: O(1)
'''

class Solution:

    def longest_common_prefix(self, strs):
        if not strs:
            return ""
        prefix = strs[0]
        k = len(prefix)
        for word in strs:
            i = 0
            while i < k and i < len(word) and prefix[i] == word[i]:
                i += 1
            k = i
        return ''.join(prefix[:k])


print(Solution().longest_common_prefix(["flower","flow","flight"]))
# fl

print(Solution().longest_common_prefix(["dog","racecar","car"]))
# ""

