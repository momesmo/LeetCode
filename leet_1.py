#!/usr/bin/env python
class Solution(object):
	def generateParenthesis(self, n):
		"""
		:type n: int
		:rtype: List[str]
		"""
		

		"""
		ex 1: [SE]											()
		ex 2: [SSEE, SESE]									(()), ()()
		ex 3: [SSSEEE, SSESEE, SSEESE, SESSEE, SESESESE]	((())), (()()), (())(), ()(()), ()()()
		"""