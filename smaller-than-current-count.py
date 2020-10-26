class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        store={}
        copy = nums[:]
        nums.sort()
        for i in range(0,len(nums)):
            if nums[i] not in store:
                store[nums[i]]=i
        output = []
        for j in range(0,len(copy)):
            output.append(store[copy[j]])
        return output