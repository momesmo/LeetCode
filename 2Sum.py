class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        k = 0
        for x in nums:
        	j = target - x
        	k += 1
        	tmp = nums[k:]
        	if j in tmp:
        		return [k-1, tmp.index(j) + k]

# [2, 7, 1, 15]
# 0: j = 15, k = 1, tmp = [7, 11, 15]
#	if 15 is in [7, 11, 15]: return [0, 3]

print Solution().twoSum([2,7,11,15], 17)