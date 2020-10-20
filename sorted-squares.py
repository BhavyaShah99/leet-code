class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        out = []
        for i in A:
            out.append(i*i)
        out = sorted(out)
        return out
        