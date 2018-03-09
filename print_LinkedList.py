def print_L(l):
	while l.next is not None:
		print str(l.val) + "->",
		l = l.next
	print l.val