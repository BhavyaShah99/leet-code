class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        tracker = {}
        for num in nums:
            try:
                tracker[str(num)] = tracker[str(num)]+1
            except KeyError:
                tracker[str(num)] = 1
        total = 0
        for keyNum in tracker:
            total += (tracker[keyNum] * (tracker[keyNum] - 1)) // 2
            
        return total