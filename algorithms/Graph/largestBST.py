'''
This problem was recently asked by Twitter:

You are given the root of a binary tree. Find and return the largest subtree of that tree, which is a valid binary search tree.

'''


class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

    def __str__(self):
        # preorder traversal
        answer = str(self.val)
        if self.left:
            answer += str(self.left)
        if self.right:
            answer += str(self.right)
        return answer

class Solution:

    def largest_bst_subtree(self, root):
        return self.largest_bst(root, 0, None)

    def largest_bst(self, root, maxheight, maxnode):
        if self.isValidBST(root, float('-inf'), float('inf')):
            size = self.size(root)
            # print(size)
            if size > maxheight:
                maxheight = size
                maxnode = root
                # print(maxnode.val, maxheight)
                return maxnode, maxheight
        if root.left:       
            n, h = self.largest_bst(root.left, maxheight, maxnode)
            if h > maxheight:
                maxheight = h
                maxnode = n
        if root.right:
            n, h = self.largest_bst(root.right, maxheight, maxnode)
            if h > maxheight:
                maxheight = h
                maxnode = n
        return maxnode

    def size(self, root):
        if not root:
            return 0
        return self.size(root.left) + 1 + self.size(root.right)

    def isValidBST(self, node, low, high):
        if not node:
            return True
        val = node.val
        if val < low or val > high:
            return False
        if not self.isValidBST(node.left, low, val):
            return False
        if not self.isValidBST(node.right, val, high):
            return False
        return True





#     5
#    / \
#   6   7
#  /   / \
# 2   4   9
node = TreeNode(5)
node.left = TreeNode(6)
node.right = TreeNode(7)
node.left.left = TreeNode(2)
node.right.left = TreeNode(4)
node.right.right = TreeNode(9)
print(Solution().largest_bst_subtree(node))
#749