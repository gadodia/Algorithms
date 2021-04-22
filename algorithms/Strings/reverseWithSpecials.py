'''
Given a string, that contains special character together with alphabets (a to z and A to Z), reverse the string in a way that special characters are not affected.

Examples:

Input:   str = "a,b$c"
Output:  str = "c,b$a"
Note that $ and , are not moved anywhere.  
Only subsequence "abc" is reversed

Input:   str = "Ab,c,de!$"
Output:  str = "ed,c,bA!$"

Time: O(n)
Space: O(n) -> converting string to list
'''

class Solution:

    def reverseStr(self, str):
        str = list(str)
        i, j = 0, len(str)-1
        while i <= j:
            while i < len(str) and not str[i].isalpha():
                i += 1
            while j >= 0 and not str[j].isalpha():
                j -= 1
            if i <= j:
                str[i], str[j] = str[j], str[i]
                i += 1
                j -= 1
        return ''.join(str)

print(Solution().reverseStr('abcdefgh'))
print(Solution().reverseStr('abcd$fgh'))
print(Solution().reverseStr('@#$abcd$fgh*'))
print(Solution().reverseStr('Ab,c,de!$'))
