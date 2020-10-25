class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        copy = heights[:]
        copy.sort()
        changes = 0
        for i in range(0,len(heights)):
            if heights[i] != copy[i]:
                changes+=1
        return changes