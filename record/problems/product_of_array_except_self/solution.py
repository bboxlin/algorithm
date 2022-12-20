class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # ans is a pre-product except itself from left to right 
        ans = [] 
        p = 1 
        for num in nums:
            ans.append(p)
            p *= num 

        # ans is now a pre-product * post-product except itself.
        posp = 1
        for i in range( len(nums)-1, -1, -1):
            ans[i] *= posp
            posp *= nums[i]
        return ans