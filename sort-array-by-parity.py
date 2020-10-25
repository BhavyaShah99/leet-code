class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        odds = []
        evens = []
        for i in range(0,len(A)):
            if A[i]%2 != 0:
                odds.append(A[i])
            else:
                evens.append(A[i])
        return evens+odds