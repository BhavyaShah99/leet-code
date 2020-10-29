class Solution:
    def generateTheString(self, n: int) -> str:
        st = ''
        if n%2 == 0:
            for i in range(0,n-1):
                st += 'o'
            st += 'h'
        else:
            for i in range(0,n):
                st += 'o'
        return st