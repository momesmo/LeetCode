class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        #final_str = ""
        final_len, tmp_len = 0, 0
        tmp_list = []
        for c in s:
        	tmp_list.append(c)
        	if len(tmp_list) != len(set(tmp_list)): #duplicate
        		tmp_list.pop()
        	

print Solution().lengthOfLongestSubstring("pwwkew")