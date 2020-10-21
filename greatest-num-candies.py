class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        tempCandies = candies[:]
        tempCandies.sort(reverse=True)
        highestPossibleCandies = tempCandies[0]
        output = []
        for candy in candies:
            if (candy + extraCandies) >= highestPossibleCandies:
                output.append(True)
            else:
                output.append(False)
        return output