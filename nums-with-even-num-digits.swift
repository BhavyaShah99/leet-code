class Solution {
    func count(num : Int) -> Int {
        var n = num
        var count = 0 
        while (n != 0) { 
            count += 1 
            n = n / 10 
        }
        return count
    }
    
    func findNumbers(_ nums: [Int]) -> Int {
        var out = 0
        for i in nums {
            if count(num : i)%2 == 0 {
                out += 1
            }
        }
        return out
    }
}