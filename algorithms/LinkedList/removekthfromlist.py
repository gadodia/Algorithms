


class Node():


    def __init__(self, v):
        self.v = v
        self.next = None


class Solution:

    def __init__(self, l, k):
        self.l = l
        self.k = k

    def removekth(self):
        slow, fast = self.l, self.l
        for _ in range(self.k):
            fast = fast.next
        if not fast:
            return self.l.next
        prev = None
        while fast:
            prev = slow
            fast = fast.next
            slow = slow.next
        prev.next = slow.next
        return self.l


if __name__ == '__main__':
    n = Node(1)
    n.next = Node(2)
    n.next.next = Node(3)
    n.next.next.next = Node(4)
    s = Solution(n, 4)
    l = s.removekth()
    res = []
    while l:
        res.append(str(l.v))
        l = l.next
    print('->'.join(res))