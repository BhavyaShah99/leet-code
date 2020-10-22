class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        pairs = 0
        for i in range(0, len(arr)):
            curr = arr[i]
            for j in range(i+1, len(arr)):
                if abs(curr-arr[j]) <= a:
                    for k in range(j+1, len(arr)):
                        if abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                            pairs += 1
        return pairs