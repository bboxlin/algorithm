class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        '''
        two extreme are left and right
        pick the max one and put it into the res list from last to first
        '''
        l, r = 0, len(nums)-1
             
        res = [0]*len(nums)
        for i in range(len(nums)-1, -1, -1):
            if abs(nums[l]) < abs(nums[r]):
                res[i] = nums[r] * nums[r]
                r -= 1
            else:
                res[i] = nums[l] * nums[l]
                l += 1
        return res
