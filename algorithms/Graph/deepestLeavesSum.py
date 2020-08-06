import collections

'''
Given a binary tree, return the sum of values of its deepest leaves.

Input: root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
Output: 15
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        self.level = collections.defaultdict(list)
        self.maxdepth = 0
        def leavesSum(node, depth):
            if not node: 
                return 0
            if not node.left and not node.right:
                self.level[depth].append(node.val)
                self.maxdepth = max(self.maxdepth, depth)
            leavesSum(node.left, depth+1)
            leavesSum(node.right, depth+1)
        leavesSum(root, 0)
        return sum(self.level[self.maxdepth])

n = TreeNode(1, TreeNode(2, TreeNode(4, TreeNode(7)), TreeNode(5)), TreeNode(3, None, TreeNode(6, None, TreeNode(8))))
print(Solution().deepestLeavesSum(n))
        