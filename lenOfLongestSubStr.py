class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        lastSame = -1
        ret = 0
        pos = {}
        for i in range(0, len(s)):
            if s[i] in pos and lastSame < pos[s[i]]:
                lastSame = pos[s[i]]
            if i - lastSame > ret:
                ret = i - lastSame
            pos[s[i]] = i
        return ret

print Solution().lengthOfLongestSubstring("dvdf")