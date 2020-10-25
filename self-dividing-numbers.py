class Solution:
    
    def isSelfDividing(self, num):
        numStr = str(num)
        for n in numStr:
            if int(n) == 0 or num%int(n) > 0:
                return False
        return True
    
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        output = []
        for num in range(left, right+1):
            if self.isSelfDividing(num) == True:
                output.append(num)
        return output