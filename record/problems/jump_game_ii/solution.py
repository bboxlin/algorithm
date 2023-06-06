class Solution:
    def jump(self, nums: List[int]) -> int:
        # BFS as a sliding window
        # each jump we maintain a [l, r] distance 
        # then go to [l, r] distance and find out the right boundaries 
        res = 0
        l, r = 0, 0
        nxtfartest = 0
        while r < len(nums) - 1:
            for i in range(l, r+1):
                nxtfartest = max(nxtfartest, i + nums[i])
            l = r + 1
            r = nxtfartest
            res += 1
        return res 
            