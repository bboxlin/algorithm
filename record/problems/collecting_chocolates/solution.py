class Solution:
    def minCost(self, nums: List[int], x: int) -> int:
        n = len(nums)
        res = math.inf
        mincost = nums[:]
        # Simulate entire shift from 0 -> n-1
        for i in range(n):
            ishiftcost = i * x
            for j in range(n):
                mincost[j] = min(mincost[j], nums[(i+j) % n])
            res = min(res, sum(mincost) + ishiftcost)
        return res
 