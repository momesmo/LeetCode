#Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def removeNthFromEnd(head, n):
    """
    :type head: ListNode
    :type n: int
    :rtype: ListNode
    """
    d = ListNode(0)
    d.next = head
    f = d
    s = d
    for i in range(0, n+1):
    	#print(f.val, "->", f.next.val)
    	f = f.next
    while f is not None:
    	f = f.next
    	s = s.next
    s.next = s.next.next
    return d.next;

# D -> 1 -> 2 -> 3 -> 4 -> 5 -> None
one = ListNode(1)
two = ListNode(2)
three = ListNode(3)
four = ListNode(4)
five = ListNode(5)
one.next = two
two.next = three
three.next = four
four.next = five

ret = removeNthFromEnd(one, 2)
while ret is not None:
	print(ret.val)
	ret = ret.next