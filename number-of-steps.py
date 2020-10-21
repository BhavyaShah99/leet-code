class Solution(object):
    def numberOfSteps (self, num):
        """
        :type num: int
        :rtype: int
        """
        currNum = num
        ct = 0
        while currNum != 0:
            if currNum%2 == 0:
                currNum = currNum/2
                ct += 1
            else:
                currNum = currNum - 1
                ct+=1
        return ct