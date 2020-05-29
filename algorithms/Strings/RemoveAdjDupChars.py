'''
This problem was recently asked by Apple:

Given a string, we want to remove 2 adjacent characters that are the same, and repeat the process with the new string until we can no longer perform the operation.

Here's an example and some starter code:

def remove_adjacent_dup(s):
  # Fill this in.

print(remove_adjacent_dup("cabba"))
# Start with cabba
# After remove bb: caa
# After remove aa: c
# print c

Time: O(n)
Space: O(n) for stack
'''

class Solution:

    def remove_adjacent_dup(self, s):
        stack = []
        for char in s:
            if stack and stack[-1] == char:
                stack.pop()
            else:
                stack.append(char)
        return ''.join(stack)
    
print(Solution().remove_adjacent_dup('cabba'))
# c
