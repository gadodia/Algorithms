'''
This problem was recently asked by Apple:

Given 2 binary trees t and s, find if s has an equal subtree in t, where the structure and the values are the same. Return True if it exists, otherwise return False.
'''

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return f"(Value: {self.value} Left: {self.left} Right: {self.right})"


class Solution:
    def find_subtree(self, s, t):
        if not t:
            return True
        if s.value == t.value:
            print(s.value, t.value)
            if self.is_subtree(s, t):
                return True
        return self.find_subtree(s, t.left) or self.find_subtree(s, t.right)
    
    def is_subtree(self, s, t):
        if not s and not t:
            return True
        if not s or not t:
            return False        
        if s.value != t.value:
            return False
        if not self.is_subtree(s.left, t.left) or not self.is_subtree(s.right, t.right):
            return False
        return True
    
  

t3 = Node(4, Node(3), Node(2))
t2 = Node(5, Node(4), Node(-1))
t = Node(1, t2, t3)

s = Node(4, Node(3), Node(10))
"""
Tree t:
    1
   / \
  4   5 
 / \ / \
3  2 4 -1

Tree s:
  4 
 / \
3  2 
"""

print(Solution().find_subtree(s, t))
# True