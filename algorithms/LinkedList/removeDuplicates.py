'''
This problem was recently asked by Amazon:

Given a sorted linked list of integers, remove all the duplicate elements in the linked list so that all elements in the linked list are unique.

Time: O(n)
Space: O(1)
'''

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return f"({self.value}, {self.next})"

class Solution:
    def remove_dup(self, lst):
        if not lst or not lst.next:
            return lst
        prev = None
        cur = lst
        while cur:
            prev = cur
            cur = cur.next
            while cur and cur.value == prev.value:
                cur = cur.next
            prev.next = cur


lst = Node(1, Node(2, Node(2, Node(3, Node(3)))))

Solution().remove_dup(lst)
print(lst)
# (1, (2, (3, None)))