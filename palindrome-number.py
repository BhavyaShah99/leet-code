class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        og = str(x)
        Reverse = 0    
        while x > 0:    
            Reminder = x %10    
            Reverse = (Reverse *10) + Reminder    
            x = x //10
        rev = str(Reverse)
        if og == rev:
            return True
        else:
            return False