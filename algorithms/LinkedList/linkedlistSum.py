'''
Prob: Given 2 linked list, return the sum of linked list representing the numbers
'''


class Node:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def sumRecursive(self, l1: Node, l2: Node) -> Node:
        def helper(a, b, carry):
            sum = a.val + b.val + carry
            carry = sum // 10
            ret = Node(sum % 10)
            if a.next or b.next:
                if not a.next:
                    a.next = Node(0)
                if not b.next:
                    b.next = Node(0)
                ret.next = helper(a.next, b.next, carry)
            elif carry:
                ret.next = Node(carry)
            return ret
        return helper(l1, l2, 0)
    
    def sumIterative(self, l1: Node, l2: Node) -> Node:
        a, b, carry = l1, l2, 0
        ret = current = None
        while a or b:
            sum = a.val + b.val + carry
            carry = sum // 10
            if not current:
                ret = current = Node(sum % 10)
            else:
                current.next = Node(sum % 10)
                current = current.next
            # print("Current: ", current.val)
            if a.next or b.next:
                if not a.next:
                    a.next = Node(0)
                if not b.next:
                    b.next = Node(0)
            elif carry:
                ret.next = Node(carry)
            a = a.next
            b = b.next
        return ret

a = Node(5)
a.next = Node(7)
b = Node(2)
b.next = Node(5)
res_recur = Solution().sumRecursive(a, b)
while res_recur:
    print(res_recur.val)
    res_recur = res_recur.next

a = Node(5)
a.next = Node(7)
b = Node(2)
b.next = Node(5)
res_iter = Solution().sumIterative(a, b)
while res_iter:
    print(res_iter.val)
    res_iter = res_iter.next