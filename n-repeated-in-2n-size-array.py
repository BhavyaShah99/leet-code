class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        N = len(A)/2
        d = {'a'}
        for i in range(0,len(A)):
            if A[i] in d:
                return A[i]
            d.add(A[i])