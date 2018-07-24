class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1
        L = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        result = 0
        sign = 1
        str = self.removeLeadingWhitespace(str)
        if str == "":
        	return result
        if str[0] == "+":
        	sign = 1
        	str = str[1:]
        elif str[0] == "-":
        	sign = -1
        	str = str[1:]
    	if str == "":
        	return result
        while len(str) > 0 and L.count(str[0]) == 1:
        	result *= 10
        	result += L.index(str[0])
        	str = str[1:]
        result *= sign
        if result < INT_MIN:
        	return INT_MIN
        if result > INT_MAX:
        	return INT_MAX
        return result

    def removeLeadingWhitespace(self, str):
    	while(str != '' and str[0] == ' '):
    		str = str[1:]
    	return str


print Solution().myAtoi("42")