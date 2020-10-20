class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        insert_index = 0
        if target < nums[0]:
            return insert_index
        for i in range(0,len(nums)):
            if nums[i] == target:
                return i
            if i+1 == len(nums):
                insert_index = len(nums)
                return insert_index
            if nums[i] < target and nums[i+1] > target:
                insert_index = i+1
                return insert_index
    