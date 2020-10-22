class Solution:
    def numTeams(self, rating: List[int]) -> int:
        pairs = 0
        if len(rating) < 3:
            return pairs
        else:
            for i in range(0, len(rating)):
                for j in range(i+1, len(rating)):
                    for k in range(j+1, len(rating)):
                        if (rating[i] < rating[j] < rating[k]) or (rating[i] > rating[j] > rating[k]):
                            pairs += 1
        return pairs