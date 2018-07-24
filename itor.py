class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        result = ""
        thousands = num / 1000
        th_rem = num % 1000
        hundreds = th_rem / 100
        h_rem = th_rem % 100
        tens = h_rem / 10
        ones = h_rem % 10

        while thousands > 0:
            result += "I"
            thousands -= 1
        while hundreds > 0:
            return result
        while tens > 0:
            return result
        while ones > 0:
            return result
        return result


if __name__ == "__main__":
    print Solution().intToRoman(999)
    print Solution().intToRoman(3999)
