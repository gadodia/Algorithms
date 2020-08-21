'''
This problem was recently asked by Google:

Given a node in a binary search tree (may not be the root), find the next largest node in the binary search tree (also known as an inorder successor). The nodes in this binary search tree will also have a parent field to traverse up the tree.


#     3
#    / \
#   2   4
#  /     \
# 1       5

Time: O(n)
Space: O(1)

'''

class Node:
  def __init__(self, value, left=None, right=None, parent=None):
    self.value = value
    self.left = left
    self.right = right
    self.parent = parent

  def __repr__(self):
    return f"(Value: {self.value}, Left: {self.left}, Right: {self.right})"

class Solution:
    def inorder_successor(self, node):
        if not node.left and not node.right:
            if node.parent and node.parent.left == node:
                return node.parent.value
            else:
                return None 
        if not node.right:
            if node.parent:
                return node.parent.value
        node = node.right
        while node.left:
            node = node.Left
        return node.value


tree = Node(3)
tree.left = Node(2)
tree.right = Node(4)
tree.left.parent = tree
tree.right.parent = tree
tree.left.left = Node(1)
tree.left.left.parent = tree.left
tree.right.right = Node(5)
tree.right.right.parent = tree.right

print(Solution().inorder_successor(tree.left))
# 3
print(Solution().inorder_successor(tree.left.left))
# 2
print(Solution().inorder_successor(tree.right))
# 5
print(Solution().inorder_successor(tree.right.right))
# None