'''
This problem was recently asked by Microsoft:

A unival tree is a tree where all the nodes have the same value. Given a binary tree, return the number of unival subtrees in the tree.

For example, the following tree should return 5:

   0
  / \
 1   0
    / \
   1   0
  / \
 1   1

The 5 trees are:
- The three single '1' leaf nodes. (+3)
- The single '0' leaf node. (+1)
- The [1, 1, 1] tree at the bottom. (+1)

Time: O(n)
Space: O(n) 
'''

class Node(object):
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

class Solution():
    
    def count_unival_subtrees(self, root):
        self.res = 0
        def is_unival_subtree(node):
            if not node:
                return True
            if not node.left and not node.right:
                self.res += 1
                return True            
            L = is_unival_subtree(node.left)
            R = is_unival_subtree(node.right) 
            if L and R:
                if (node.left and node.val != node.left.val) or (node.right and node.val != node.right.val):
                    return False
                else:
                    self.res += 1
                    return True
            return False
        is_unival_subtree(root)
        return self.res
            


a = Node(0)
a.left = Node(1)
a.right = Node(0)
a.right.left = Node(1)
a.right.right = Node(0)
a.right.left.left = Node(1)
a.right.left.right = Node(1)

print(Solution().count_unival_subtrees(a))
# 5

a = Node(0)
print(Solution().count_unival_subtrees(a))
# 1

a = None
print(Solution().count_unival_subtrees(a))
# 0