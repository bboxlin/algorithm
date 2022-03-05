import collections
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        
        # [1, 2, 3]
        # e1 e2 curearn
        # check for max(e1+curearn, e2)
         
        count = collections.Counter(nums)
        e1, e2 = 0, 0
        nums = list(set(nums))
        for i in range(len(nums)):
            cur_earn = nums[i]*count[nums[i]]
            if i > 0 and (nums[i] == nums[i-1]+1 or nums[i] == nums[i-1]-1):
                tmp = e2
                e2 = max(e1+cur_earn, e2)
                e1 = tmp
            else:
                tmp = e2
                e2 = cur_earn + e2
                e1 = tmp
        return e2
            
            
        