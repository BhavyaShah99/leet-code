class Solution:
    def balancedStringSplit(self, s: str) -> int:
        balance = 0
        balancedStrings = 0
        for i in range(0, len(s)):
            if i>0 and balance == 0:
                balancedStrings += 1
            if s[i] == 'L':
                balance += 1
            else:
                balance -= 1
        if balance == 0:
            balancedStrings += 1
        return balancedStrings