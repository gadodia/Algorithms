'''
Prob: Given ransom note string and a string containing letters from magazines, return if note can be constructed from the letters.
Brute Force: For each char in note, loop over all chars from magazines and if found, remove it from the magazine string and continue else return false. Time complexity: O(m*n), Space O(1)
Optimize approach: Construct hashmap with chars and its count from magazines string. Loop over note chars and keep reducing the count from hashmap.

Time: O(n)
Space: O(n)
'''

import collections


class Solution:

    def can_construct(self, ransomNote: str, magazines: str) -> bool:
        mag_map = collections.defaultdict(int)
        for char in magazines:
            mag_map[char] += 1
        for char in ransomNote:
            mag_map[char] -= 1
            if mag_map[char] < 0:
                return False
        return True
    
    def canConstructV2(self, ransomNote: str, magazine: str) -> bool:
        if not magazine and not ransomNote:
            return True
        notemap = collections.defaultdict(int)
        for char in ransomNote:
            notemap[char] += 1
        if not notemap:
            return True
        for char in magazine:
            if char in notemap:
                notemap[char] -= 1
                if notemap[char] <= 0:
                    del notemap[char]
                if not notemap:
                    return True
        return False


print(Solution().can_construct('aa', 'aab'))
print(Solution().can_construct('aa', 'ab'))
