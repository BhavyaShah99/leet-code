class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(0, len(nums)):
            d[nums[i]] = i
        for j in range(0, len(nums)):
            sub = target - nums[j]
            if sub in d:
                if d[sub] != j:
                    return j, d[sub]
        return -1
