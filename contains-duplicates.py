class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums2 = nums
        nums2.sort()
        for i in range(0,len(nums2)):
            if i+1<len(nums2):
                if nums2[i] == nums2[i+1]:
                    return True
        return False