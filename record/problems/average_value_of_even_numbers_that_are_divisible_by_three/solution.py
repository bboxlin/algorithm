class Solution:
    def averageValue(self, nums: List[int]) -> int:
        total, cnt = 0, 0
        for num in nums:
            if num % 2 == 0 and  num % 3 == 0:
                total += num
                cnt += 1
        return total//cnt if cnt != 0 else 0