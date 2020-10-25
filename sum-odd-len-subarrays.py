class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        sumOfOddSubs = sum(arr)
        for i in range(0,len(arr)):
            newSub = [arr[i]]
            for j in range(i+1,len(arr)):
                newSub.append(arr[j])
                if len(newSub)%2!=0:
                    sumOfOddSubs += sum(newSub)
        return sumOfOddSubs