from itertools import takewhile, dropwhile
from typing import List

'''
Given array, generate tree
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def __str__(self):
        result = " "
        result += str(self.val)
        if self.left:
            result += str(self.left)
        if self.right:
            result += str(self.right)
        return result

#----------- LEVEL ORDER ---------
class SolutionLevelOrder:

    def generateTree(self, arr):
        def formTree(arr, index):            
            if index < len(arr):
                if not arr[index]:
                    return None
                node = TreeNode(arr[index])
                node.left = formTree(arr, 2*index+1)
                node.right = formTree(arr, 2*index+2)
                return node
            return None
        return formTree(arr, 0)
        
        

print(SolutionLevelOrder().generateTree([5,3,6,2,4,None,None,1]))


#----------- PRE ORDER ---------
class SolutionPreorder:

    def print_level_order(self, node):
        queue = []
        queue.append(node)
        result = []
        while queue:
            temp_queue = []
            size = len(queue)
            for _ in range(size):
                node = queue.pop(0)
                if not node:
                    result.append("null")
                else:
                    result.append(node.val)
                    if not node.left and not node.right:
                        continue
                    temp_queue.append(node.left)
                    temp_queue.append(node.right)
            queue += temp_queue
        return result

        
        
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if not preorder:
            return None
        stack = []
        root = node = TreeNode(preorder[0])
        stack.append(node)        
        for j in range(1, len(preorder)):
            if preorder[j] < preorder[j-1]:
                node.left = TreeNode(preorder[j])
                node = node.left
                stack.append(node)
            else:
                while stack and preorder[j] > stack[-1].val:
                    node = stack.pop()
                node.right = TreeNode(preorder[j])
                node = node.right
                stack.append(node)
        return root
    
    def bstFromPreorderRecursion(self, preorder: List[int]) -> TreeNode:
        if preorder:
            return TreeNode(preorder[0],
                            self.bstFromPreorderRecursion(tuple(takewhile(lambda x:x<preorder[0], preorder[1:]))),
                            self.bstFromPreorderRecursion(tuple(dropwhile(lambda x:x<preorder[0], preorder[1:]))))
    


node = SolutionPreorder().bstFromPreorder([8,5,1,7,10,12])
print(SolutionPreorder().print_level_order(node))

#----------- IN ORDER ---------
class SolutionInorder:


    def bstfrominorder(self, inorder: List[int]) -> TreeNode:
        return self.bsthelper(inorder, 0, len(inorder)-1)

    def bsthelper(self, inorder, low, high):
        if low <= high:
            mid = low + (high-low)//2 
            root = TreeNode(inorder[mid])
            root.left = self.bsthelper(inorder, low, mid-1)
            root.right = self.bsthelper(inorder, mid+1, high)
            return root
        return None

    
print(SolutionInorder().bstfrominorder([1,2,3,4,5,6,7,8,9,10]))