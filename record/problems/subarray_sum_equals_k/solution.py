class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # presum : freq
        memo = {0 : 1}
        cursum = 0
        res = 0
        for n in nums:
            cursum += n
            if cursum - k in memo.keys():
                res += memo[cursum - k]
       
            if cursum not in memo:
                memo[cursum] = 1
            else:
                memo[cursum] += 1
        return res
