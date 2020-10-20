class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        out = 0
        n = False
        if x<0:
            n = True
        x = abs(x)
        while x!=0:
            out *= 10
            out += x%10
            x = x/10
        if out > 2147483647 or -out < -2147483648:
            return 0
        if n:
            return -out
        return out