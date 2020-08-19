'''
Question 1 :
Imagine that an employment tree represents the formal employee hierarchy at Amazon. Manager nodes have
chid nodes for each employee that reports to them; each of these employees can, in turn, have child nodes
representing their respective reportees. Each node in the tree contains an integer representing the number of
months the employee has spent at the company. Team tenure is computed as the average tenure of the manager
and all the company employees working below the manager. The oldest team has the highest team tenure.

Write an algorithm to find the manager of the team with the highest tenure. An employee must have child nodes
to be a manager.

Input
The input to the function/method consists of an argument -
president, a node representing the root node of the employee hierarchy.

Output
Return the node which has the oldest team.

Note
There will be at least one child node in the tree and there will be no ties.

Example

Input
   President =
	             20
          12            18
             
      11   2   3      15   8

Output = 18
Explanation :
There are three managers in this tree with the following team tenures :
12 => (11+2+3+12)/4 = 7
18 => (18+15+8)/3 = 13.67
20 => (12+11+2+3+18+15+8+20)/8 = 11.125

Time: O(n)
Space: O(n)
'''

class Node:
    def __init__(self, val, children=[]):
        self.val = val
        self.children = children
        
class Solution:

    def maxTenure(self, root):
        self.max_tenure = 0.0
        self.max_tenure_manager = 0
        def calcTenure(node):
            if not node:
                return 0
            if not any(child for child in node.children):
                node.employees = 0
                return node.val
            node.employees = 0            
            total_sum = sum(calcTenure(child) for child in node.children)
            for child in node.children:
                node.employees = node.employees + child.employees + 1
            total_sum += node.val
            avg = total_sum/(node.employees+1)
            if self.max_tenure < avg:
                self.max_tenure = avg
                self.max_tenure_manager = node.val
            return total_sum
        calcTenure(root)
        return self.max_tenure_manager


# n = Node(20)
# n.children.append(Node(12).children.append(Node(11)).append(Node(2)).append(Node(3))).append(Node(18).children.append(Node(15)).append(Node(8)))


n = Node(20, [Node(12, [Node(11), Node(2), Node(3)]), Node(18, [Node(15), Node(8)])])
print(Solution().maxTenure(n) == 18)

n = Node(20, [Node(12, [Node(11), Node(2), Node(3)]), Node(18, [Node(15), Node(8)]), Node(50)])
print(Solution().maxTenure(n) == 20)