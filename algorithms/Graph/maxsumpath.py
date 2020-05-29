
'''
***** NOT SOLVED YET *****

This problem was recently asked by Facebook:

You are given the root of a binary tree. Find the path between 2 nodes that maximizes the sum of all the nodes in the path, and return the sum. The path does not necessarily need to go through the root.

'''

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
class Solution:

    def maxPathSum(self, root, maxsum):
        if not root:
            return 0
        currmaxsum = self.maxSumHelper(root, 0, float('-inf'))
        # print(currmaxsum)     
        maxsum = max(currmaxsum, maxsum)
        return self.maxPathSum(root.left, maxsum) + root.val + self.maxPathSum(root.right, maxsum)

    def maxSumHelper(self, node, currentsum, maxsum):
        if not node:
            return max(currentsum, maxsum)
        # else:
        #     currentsum = currentsum + node.val
        #     maxsum = max(maxsum, currentsum)
        return node.val + self.maxSumHelper(node.left, currentsum, maxsum) + self.maxSumHelper(node.right, currentsum, maxsum)
        

# (* denotes the max path)
#       *10
#       /  \
#     *2   *10
#     / \     \
#   *20  1    -25
#             /  \
#            3    4
root = Node(10)
root.left = Node(2)
root.right = Node(10)
root.left.left = Node(20)
root.left.right = Node(1)
root.right.right = Node(-25)
root.right.right.left = Node(3)
root.right.right.right = Node(4)
print(Solution().maxPathSum(root, 0))
# 42