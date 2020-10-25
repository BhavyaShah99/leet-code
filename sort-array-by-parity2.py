class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        odds = []
        evens = []
        for i in range(0,len(A)):
            if A[i]%2 != 0:
                odds.append(A[i])
            else:
                evens.append(A[i])
        output = []
        for j in range(0, len(A)):
            if j%2 != 0:
                output.append(odds.pop(-1))
            else:
                output.append(evens.pop(-1))
        return output