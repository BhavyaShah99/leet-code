class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        symbols = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        exceptions = ['IV', 'IX', 'XL', 'XC', 'CD', 'CM']
        answer = 0
        char = 0
        while char < len(s):
            if char+1 < len(s) and s[char]+s[char+1] in exceptions:
                answer += (symbols[s[char+1]]-symbols[s[char]])
                char += 2
            else:
                answer += symbols[s[char]]
                char += 1
        return answer  