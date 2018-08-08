class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """

        # RECURSIVE METHOD

        # final case when no pattern left, check if string is complete or not
        if not p:
            if not s:
                return True
            else:
                return False
        # last pattern element or next element is not *
        if len(p) == 1 or p[1] != '*':
            # recurs by stripping first element of s and p
            # False if s DNE or first elements of s and p aren't same
            if len(s) > 0 and (p[0] == s[0] or p[0] == '.'):
                return self.isMatch(s[1:], p[1:])
            else:
                return False
        # not last element and next is *
        else:
            while len(s) > 0 and (p[0] == s[0] or p[0] == '.'):
                if self.isMatch(s, p[2:]):
                    return True
                s = s[1:]
            return self.isMatch(s, p[2:])


print(Solution().isMatch('aaaaaaaaaaaaab', 'a*a*a*a*a*a*a*a*a*a*b'))
