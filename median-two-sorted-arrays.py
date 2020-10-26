class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        full_array = nums1 + nums2
        full_array.sort()
        if len(full_array)%2==0:
            b = len(full_array)//2 - 1
            t = (len(full_array)//2 + 1) -1
            return (full_array[b]+full_array[t])/2
        else:
            return full_array[len(full_array)//2]
            