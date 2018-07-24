class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
        	return s
        L = []
        result = ""
        flag = True # True = increasing, False = decreasing
        index = 0
        # setup list L, with # of elements = numRows
        for x in range(0, numRows):
        	L.append("")
        # zigzag conversion
        for c in s:
        	print(index)
        	L[index] += c
        	if flag:
        		index += 1
        	else:
        		index -= 1
        	if index == numRows-1:
        		flag = False
        	elif index == 0:
        		flag = True
        # create final string for returning
        for i in L:
        	result += i
        return result

print Solution().convert("AB", 1)
