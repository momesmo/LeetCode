class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        tmp_diff, diff, j, k, lastI = 0, float('inf'), 0, len(nums) - 1, len(nums) - 2
        for i in range(0, lastI - 1):
            j, k = i + 1, lastI + 1
            while j < k:
            	tmp_diff = nums[i] + nums[j] + nums[k] - target
            	if tmp_diff == 0: return target
            	if abs(tmp_diff) < diff: diff = abs(tmp_diff)
                if tmp_diff < 0: j+=1
                else: k-=1
        return diff

print Solution().threeSumClosest([1, 1, -1, -1, 3], 3)