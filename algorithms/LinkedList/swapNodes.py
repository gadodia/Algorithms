'''
Given a linked list, swap every two adjacent nodes and return its head.

You may not modify the values in the list's nodes, only nodes itself may be changed.

 

Example:

Given 1->2->3->4, you should return the list as 2->1->4->3.

Time: O(n)
Space: O(n)
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        res = ""
        res += str(self.val)        
        if self.next:
            res += "->"
            res += str(self.next)
        return res


class Solution:
    
    def swap_nodes(self, head):
        if not head or not head.next:
            return head
        prev = head
        cur = head.next
        p = self.swap_nodes(cur.next)
        cur.next = prev
        prev.next = p
        return cur

l = ListNode(1)
l.next = ListNode(2)
l.next.next = ListNode(3)
l.next.next.next = ListNode(4)
print(Solution().swap_nodes(l))
# 2->1->4->3


l = ListNode(1)
l.next = ListNode(2)
l.next.next = ListNode(3)
l.next.next.next = ListNode(4)
l.next.next.next.next = ListNode(5)
l.next.next.next.next.next = ListNode(6)
print(Solution().swap_nodes(l))
# 2->1->4->3->6->5


