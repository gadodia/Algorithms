'''
This problem was recently asked by Google:

Given a binary tree, find and return the largest path from root to leaf.


#    1
#  /   \
# 3     2
#  \   /
#   5 4


#    1
#  /   \
# 3     2
#  \   / \
#   5 4   7

'''
from typing import List
import collections

class Node:
  def __init__(self, value, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right

class Solution:
    
    def largest_path_sum(self, root: Node) -> List[int]:
        self.lpath = {}
        self.lsum = float("-inf")
        def largest_path_sum(node, path, cursum):
            if not node:
                return
            path.append(node.value)
            cursum += node.value
            if not node.left and not node.right:
                if cursum > self.lsum:
                    self.lsum = cursum
                    self.lpath = list(path)
            else:
                largest_path_sum(node.left, path, cursum)
                largest_path_sum(node.right, path, cursum)
            path.pop()
        largest_path_sum(root, [], 0)
        return self.lpath

    def paths_with_sum(self, root: Node, sum: int) -> int:         
        count = 0
        h = collections.defaultdict(int)
        def paths(node, cursum):
            nonlocal count
            if not node:
                return
            cursum += node.value
            if cursum == sum:
                count += 1
            count += h[cursum-sum]
            h[cursum] += 1
            paths(node.left, cursum)
            paths(node.right, cursum)
            h[cursum] -= 1
        paths(root, 0)
        return count


tree = Node(1)
tree.left = Node(3)
tree.right = Node(2)
tree.right.left = Node(4)
tree.left.right = Node(5)

print(Solution().largest_path_sum(tree))
# [1, 3, 5]

tree.right.right = Node(7) # Added a node
print(Solution().largest_path_sum(tree))
# [1, 2, 7]

print(Solution().paths_with_sum(tree, 8))
# 1

print(Solution().paths_with_sum(tree, 7))
# 2