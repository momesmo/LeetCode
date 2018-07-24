class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        three
        """
        s = str(x)
        if len(s) == 0 or len(s) == 1:
        	return True
        if len(s) % 2 == 0:
        	i = len(s)/2
        	j = len(s)/2 - 1
        else:
        	i = j = len(s)/2
        while i < len(s) and j >= 0:
        	if s[i] == s[j]:
        		i += 1
        		j -= 1
        	else:
        		return False
        return True

print Solution().isPalindrome(124542)