class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        tmp_len, final_len = 0, 0
        tmp_str, final_str = "", ""
        for i in range(0, len(s)):
        	for j in range(i, len(s)):
        		tmp_str += s[j]
        		if(tmp_str[::-1] == tmp_str and len(tmp_str) > final_len): #palindrome checker
        			final_len = len(tmp_str)
        			final_str = tmp_str
        	tmp_str = ""
        return final_str


print Solution().longestPalindrome("cbbd");