class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        final_len, tmp_len, i = 0, 0, 0
        final_list, tmp_list = [], []

        while i < len(s):
        	tmp_list.append(s[i])
        	print "Temp List:", tmp_list
        	if len(tmp_list) != len(set(tmp_list)): #duplicate found
        		tmp_list.pop()
        		print "Popped", s[i], ":", tmp_list
        		tmp_len = len(tmp_list)
        		if tmp_len > final_len:
        			final_len = tmp_len
        			final_list = tmp_list
        			print "Temp Final List:", final_list
        		i = tmp_list.index(s[i])
        		tmp_list = []
        		print "Logged and Reset to:", i
        		# print "Cleared & Adding:", j, tmp_list[j], tmp_list[j+1]
        		# tmp_list = list(tmp_list[j+1])
        		# print "Cleared & Added:", j, tmp_list
        	#print "No Dupe, Checking if at end...", len(tmp_list), len(set(tmp_list)), i, len(s) - 1
        	i += 1;
    	if len(tmp_list) == len(set(tmp_list)):
    		tmp_len = len(tmp_list)
    		print "Reached End, No Dupe, & Longer:", tmp_list
    		if(tmp_len > final_len):
        		final_len = tmp_len
        		final_list = tmp_list
        print "Final List:", final_list
        return final_len

print Solution().lengthOfLongestSubstring("aab")