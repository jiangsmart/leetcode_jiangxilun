# coding=utf-8
class Solution:
    def deleteDuplication(self, pHead):
        # write code here
        if not pHead:
            return None
        if pHead.next and pHead.val != pHead.next.val:
            pHead.next = self.deleteDuplication(pHead.next)
            return pHead
        else:
            p = pHead
            while p and pHead.val == p.val:
                p = p.next
            if not p:
                return None
            p.next = self.deleteDuplication(p.next)
            if p.next == None:
                return None
            return p

    def deleteDuplication2(self, pHead):
        # write code here
        if pHead is None or pHead.next is None:
            return pHead
        head1 = pHead.next
        if head1.val != pHead.val:
            pHead.next = self.deleteDuplication2(pHead.next)
        else:
            while pHead.val == head1.val and head1.next is not None:
                head1 = head1.next
            if head1.val != pHead.val:
                pHead = self.deleteDuplication2(head1)
            else:
                return None
        return pHead


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


a = ListNode(1)
b = ListNode(4)
c = ListNode(4)
d = ListNode(4)
e = ListNode(4)
f = ListNode(5)
g = ListNode(5)
a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
f.next = g
s = Solution()
# s.deleteDuplication(a)
a = s.deleteDuplication(a)
p = a
while p:
    print p.val
    p = p.next
