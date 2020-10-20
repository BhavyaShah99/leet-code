class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        s = num
        while s >= 10:
            temp = s
            s = 0
            while temp != 0:
                digit = temp % 10
                temp /= 10
                s += digit
        return s