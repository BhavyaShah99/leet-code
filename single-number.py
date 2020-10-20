class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        singles = []
        for i in nums:
            if i not in singles:
                singles.append(i)
            else:
                singles.remove(i)
        return singles[0]