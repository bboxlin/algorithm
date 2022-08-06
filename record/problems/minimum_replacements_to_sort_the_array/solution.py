class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        ans = 0
        last = nums[-1]
        n = len(nums)
        for i in range(n-2, -1, -1):
            if nums[i] > last:
                # 求 nums[i] 除以 last 向上取整
                k = (nums[i] + last - 1) // last
                ans += k - 1;
                last = nums[i] // k
            else:
                last = nums[i]
        return ans