class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        presum = [0]*(len(nums)+1)
        cursum = 0
        for i in range(1, len(presum)):
            presum[i] = nums[i-1]+cursum
            cursum = presum[i]        
        # [0, 1, 1]
        # 
        premod = set()
        for i in range(2,len(presum)):
            rj = presum[i] % k
            ri = presum[i-2] % k
            premod.add(ri)
            if rj in premod: return True      
        return False
        