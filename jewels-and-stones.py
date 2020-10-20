class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        out = 0
        for i in S:
            if i in J:
                out += 1
        return out