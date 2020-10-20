class Solution(object):
    def decompressRLElist(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        def decomp(arr, i):
            out = []
            if i < len(nums):
                for k in range(0, arr[i]):
                    out.append(arr[i+1])
                out += decomp(arr, i+2)
            return out
        return decomp(nums, 0)