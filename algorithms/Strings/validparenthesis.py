'''
This problem was recently asked by Uber:

Imagine you are building a compiler. Before running any code, the compiler must check that the parentheses in the program are balanced. Every opening bracket must have a corresponding closing bracket. We can approximate this using strings.

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
- Open brackets are closed by the same type of brackets.
- Open brackets are closed in the correct order.
- Note that an empty string is also considered valid.

Example:
Input: "((()))"
Output: True

Input: "[()]{}"
Output: True

Input: "({[)]"
Output: False

Time: O(n)
Space: O(n)
'''


class Solution:
    def isValid(self, s):
        if not s:
            return True
        stack = []
        b_map = {')':'(', '}':'{', ']':'['}
        open_b = ['(','{','[']
        close_b = [']', '}', ')']
        for b in s:
            if b in open_b:
                stack.append(b)
            elif b in close_b:
                if not stack:
                    return False
                elif stack[-1] != b_map.get(b):
                    return False
                else:
                    stack.pop()
        if stack:
            return False
        else:
            return True

    

# Test Program
s = "()(){(())" 
# should return False
print(Solution().isValid(s))

s = ""
# should return True
print(Solution().isValid(s))

s = "([{}])()"
# should return True
print(Solution().isValid(s))
