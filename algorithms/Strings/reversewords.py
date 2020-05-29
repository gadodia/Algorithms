'''
This problem was recently asked by Facebook:

Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

Example 1:
Input: "The cat in the hat"
Output: "ehT tac ni eht tah"
Note: In the string, each word is separated by single space and there will not be any extra space in the string.

Time: O(n)
Space: O(n)
'''

class Solution:
    def reverseWords(self, str):
        i,j = 0,0
        new_str = ""
        for j in range(len(str)):
            if str[j] == " ":
                new_str += self.reverseword(str[i: j])
                i = j+1
                new_str += " "
        
        return new_str + self.reverseword(str[i:j+1])


    def reverseword(self, word):
        i = 0
        j = len(word)-1
        word = list(word)
        while i < j:
            word[i], word[j] = word[j], word[i]
            i += 1
            j -= 1            
        return ''.join(word)

print(Solution().reverseWords("The cat in the hat"))
# ehT tac ni eht tah