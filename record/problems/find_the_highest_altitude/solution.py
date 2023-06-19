class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        res = 0
        cur = 0
        for num in gain:
            cur += num
            res = max(cur, res)
        return res