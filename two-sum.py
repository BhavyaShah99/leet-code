class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result_list = []
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if nums[j] == target - nums[i]:
                    result_list.append(i)
                    result_list.append(j)
                    return result_list