class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        first_half = nums[0:n]
        second_half = nums[n:len(nums)]
        print(first_half)
        print(second_half)
        shuffled = []
        for i in range(0,n):
            shuffled.append(first_half[i])
            shuffled.append(second_half[i])
        return shuffled
        