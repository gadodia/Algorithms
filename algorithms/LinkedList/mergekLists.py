'''
Merge two sorted linked lists and return it as a new sorted list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->3->5, 2->4->6
Output: 1->2->3->4->5->6

Input: 1->2->3->4->5->6, 5->8->9, 7->9->10
Output: 1->2->3->4->5->5->6->7->8->9->9->10

merge 2 lists:
Time: O(n)
Space: O(1)

merge k lists:
Time: O(n)
Space: O(n)  -> Since creating new list of nodes
'''



# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __str__(self) -> str:
        c = self
        answer = ""
        while c:
            answer += str(c.val) if c.val else ""
            c = c.next
        return answer


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = cur = ListNode(0)
        while l1 or l2:
            if not l1:
                cur.next = l2
                l2 = l2.next
                
            elif not l2:
                cur.next = l1
                l1 = l1.next
            else:
                if l1.val <= l2.val:
                    cur.next = l1
                    l1 = l1.next
                else:
                    cur.next = l2
                    l2 = l2.next
            cur = cur.next
        return head.next
    
    def mergeKLists(self, lists: list) -> ListNode:
        head = cur = ListNode(-1)
        while any(lst is not None for lst in lists):
            cur_min, i = min((c.val, i) for i, c in enumerate(lists) if c is not None)
            lists[i] = lists[i].next
            cur.next = ListNode(cur_min)
            cur = cur.next
        return head.next



a = ListNode(1, ListNode(3, ListNode(5)))
b = ListNode(2, ListNode(4, ListNode(6)))

print(a)
# 135
print(b)
# 246
c = Solution().mergeTwoLists(a, b)
print(c)
# 123456

d = ListNode(5, ListNode(8, ListNode(9)))
e = ListNode(7, ListNode(9, ListNode(10)))
print(Solution().mergeKLists([c, d, e]))
# 1234556789910