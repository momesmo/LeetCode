import math
class Solution(object):
	def median(self, lst):
		n = len(lst)
		lst = sorted(lst)
		if n < 1:
			return None
		if n % 2 == 1:
			return lst[int(math.ceil(n / 2))]
		else:
			return (lst[n//2-1] + lst[n//2])/2.0

	def findMedianSortedArrays(self, nums1, nums2):
	    """
	    :type nums1: List[int]
	    :type nums2: List[int]
	    :rtype: float
	    """
	    comboList = []
	    while len(nums1) > 0 or len(nums2) > 0:
	    	if(len(nums1) > 0 and len(nums2) > 0 and nums1[0] < nums2[0]):
	    		#print "Added", nums1[0]
	    		comboList.append(nums1[0])
	    		nums1.pop(0)
	    	if(len(nums1) > 0 and len(nums2) > 0 and nums1[0] > nums2[0]):
	    		#print "Added", nums2[0]
	    		comboList.append(nums2[0])
	    		nums2.pop(0)
	    	if(len(nums1) > 0):
	    		#print "Added", nums1[0]
	    		comboList.append(nums1[0])
	    		nums1.pop(0)
	    	if(len(nums2) > 0):
	    		#print "Added", nums2[0]
	    		comboList.append(nums2[0])
	    		nums2.pop(0)
	    	#print comboList, nums1, nums2
	    return Solution().median(comboList)

print Solution().findMedianSortedArrays([1,3], [2])