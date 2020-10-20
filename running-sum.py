class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        running_sum = nums[0]
        result = [nums[0]]
        for i in range(1,len(nums)):
            running_sum += nums[i]
            result.append(running_sum)
        return result