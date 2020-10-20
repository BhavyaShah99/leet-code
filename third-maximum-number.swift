class Solution {
    func thirdMax(_ nums: [Int]) -> Int {
        if nums.count == 0 {
            return 0
        }
        if nums.count < 3 {
            return nums.max()!
        }
        let sorted = Array(nums.sorted().reversed())
        var max_num = 1
        var third_max = sorted.max() as! Int
        for i in 0..<sorted.count {
            if max_num == 3 {
                return third_max
            }
            if sorted[i] < third_max {
                third_max = sorted[i]
                max_num += 1
            }
        }
        if max_num != 3 {
            return sorted.max()!
        }
        return third_max
    }
}