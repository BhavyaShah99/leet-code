class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        inpu = n
        prod = 1
        summed = 0
        while inpu != 0:
            digit = inpu % 10
            inpu = inpu / 10
            prod *= digit
            summed += digit
        return prod - summed