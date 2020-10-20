class Solution {
    func removeDuplicates(_ nums: inout [Int]) -> Int {
        if nums.count == 0 {
            return 0
        }
        var ct = 0
        for j in 1..<nums.count {
            if nums[j] != nums[ct] {
                ct += 1
                nums[ct] = nums[j]
            }
        }
        return ct + 1
    }
}