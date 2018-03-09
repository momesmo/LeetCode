from print_LinkedList import print_L
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        d = ListNode(0)
        curr, carry = d, 0
        while l1 or l2:
        	s = carry
        	if l1:
        		s += l1.val
        		l1 = l1.next
        	if l2:
        		s += l2.val
        		l2 = l2.next
        	carry, s = divmod(s, 10) # divmod() -> (/, %)
        	curr.next = ListNode(s)
        	curr = curr.next
        if carry == 1:
        	curr.next = ListNode(1)
        return d.next


a, a.next, a.next.next = ListNode(2), ListNode(4), ListNode(3)
b, b.next, b.next.next = ListNode(5), ListNode(6), ListNode(4)

ret = Solution().addTwoNumbers(a, b)
print_L(a)
print "+"
print_L(b)
print "="
print_L(ret)