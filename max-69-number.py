class Solution(object):
    def maximum69Number (self, num):
        """
        :type num: int
        :rtype: int
        """
        strNum = str(num)
        currMax = num
        arr = []
        for number in strNum:
            arr.append(number)
        for i in range(0,len(arr)):
            arrTemp = arr[:]
            if arrTemp[i] == '9':
                arrTemp[i] = '6'
            else:
                arrTemp[i] = '9'
            newMax = ''
            for newNum in arrTemp:
                newMax += newNum
            if int(newMax) > currMax:
                currMax = newMax
                
        return currMax