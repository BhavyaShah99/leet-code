class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        for row in grid:
            if row[len(row)-1] < 0:
                for i in range(len(row)-1,-1,-1):
                    if row[i] < 0:
                        count += 1
        return count