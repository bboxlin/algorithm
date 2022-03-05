class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0
        i, N = 0, len(nums)
        while i <= max_reach and i < N:
            max_reach = max(max_reach, i + nums[i])
            if max_reach >= N-1: return True
            i += 1
        return max_reach >= N-1