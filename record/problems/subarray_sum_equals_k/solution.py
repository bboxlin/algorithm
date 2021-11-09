class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        '''
        nums = [1,2,3,2,1]
        cursum = 1,3,6,8,9
        memo = {0: 1, 1: 1, 3: 1, 6: 1, 8: 1, 9: 1}
        '''
        memo = {0 : 1}
        cursum = 0
        res = 0
        for n in nums:
            cursum += n
            rem = cursum - k
            if rem in memo.keys():
                res += memo[rem]
                
            if cursum not in memo:
                memo[cursum] = 1
            else:
                memo[cursum] += 1
        return res