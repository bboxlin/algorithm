class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:

        def findK(cap):
            cnt = 0
            i = 0
            while i < len(nums):
                if cap >= nums[i]:
                    i += 2
                    cnt += 1
                else:
                    i += 1
            return cnt >= k

        low = min(nums)
        high = max(nums)
        while low < high:
            mid = (low + high) // 2
            if findK(mid):
                high = mid
            else:
                low = mid + 1
        return low

