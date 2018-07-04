class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        fin_start, fin_end, fin_len = 0, 0, 0        
        for i in range(0, len(s)):
            len_even, e_L, e_R = self.checkFromCenter(s, i, i+1)
            len_odd, o_L, o_R = self.checkFromCenter(s, i, i)
            if len_even > len_odd and len_even > fin_len:
                fin_len = len_even
                fin_start = e_L
                fin_end = e_R
            if len_odd > len_even and len_odd > fin_len:
                fin_len = len_odd
                fin_start = o_L
                fin_end = o_R
        return s[fin_start+1 : fin_end]


    def checkFromCenter(self, s, i1, i2):
        """
        :type s: str
        :type i1: int
        :type i2: int
        :rtype: int
        """
        R, L = i1, i2
        while L >= 0 and L < len(s) and R < len(s) and s[L] == s[R]:
            L -= 1
            R += 1
        return R - L - 1, L, R


print Solution().longestPalindrome("babad");
# print Solution().checkFromCenter("cbbd", 4, 4)