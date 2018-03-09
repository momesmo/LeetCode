class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        tmp = 0
        closest_sum = 10000000000
        for x in range(0, len(nums)-2):
        	tmp = nums[x] + nums[x+1] + nums[x+2]
        	if abs(tmp - target) < abs(closest_sum - target):
        		closest_sum = tmp
        	print closest_sum, tmp
        return closest_sum

print Solution().threeSumClosest([1, 1, -1, -1, 3], 3)