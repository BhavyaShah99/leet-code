class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip()
        try:
            num = float(s)
        except: 
            return False
        return True