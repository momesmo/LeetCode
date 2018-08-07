class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums = sorted(nums)
        min_diff, result, i = float('inf'), float('inf'), 0
        while i < len(nums) - 2:
            if i == 0 or nums[i] != nums[i - 1]:
                j, k = i + 1, len(nums) - 1
                while j < k:
                    diff = nums[i] + nums[j] + nums[k] - target
                    # print(i, j, k, '-', min_diff, diff)
                    if abs(diff) < min_diff:
                        min_diff = abs(diff)
                        result = nums[i] + nums[j] + nums[k]
                    if diff == 0:
                        return target
                    elif diff < 0:
                        j += 1
                    else:
                        k -= 1
            i += 1
        return result


print(Solution().threeSumClosest([-1, 2, 1, -4], 1))
