class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        neg = 1
        if x < 0:
        	neg = -1
        	x *= -1
        power = 0
        result = 0
        strx = str(x)
        for i in strx:
        	result += (int(i) * (10**power))
        	power += 1
        result *= neg
        if result > 2**31 - 1 or result < -2**31:
        	return 0
        return result

print(Solution().reverse(-123))