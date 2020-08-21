'''
This problem was recently asked by LinkedIn:

Given a binary tree, find the most frequent subtree sum.

Example:

   3
  / \
 1   -3

The above tree has 3 subtrees. The root node with 3, and the 2 leaf nodes, which gives us a total of 3 subtree sums. The root node has a sum of 1 (3 + 1 + -3), the left leaf node has a sum of 1, and the right leaf node has a sum of -3. Therefore the most frequent subtree sum is 1.

If there is a tie between the most frequent sum, you can return any one of them.

Time: O(n)
Space: O(n)
'''
import collections

class Node():
  def __init__(self, value, left=None, right=None):
    self.val = value
    self.left = left
    self.right = right

class Solution:
    def most_freq_subtree_sum(self, root):
        self.freq = collections.defaultdict(int)
        def subtree_sum(node):
            if not node:
                return 0
            if not node.left and not node.right:
                self.freq[node.val] += 1
                return node.val
            left_sum = subtree_sum(node.left)
            right_sum = subtree_sum(node.right)
            total_sum = left_sum + right_sum + node.val
            self.freq[total_sum] += 1
            return total_sum
        subtree_sum(root)
        k_max, v_max = 0, 0
        for k, v in self.freq.items():
            if v > v_max:
                k_max = k
                v_max = v
        return k_max



root = Node(3, Node(1), Node(-3))
print(Solution().most_freq_subtree_sum(root))
# 1
