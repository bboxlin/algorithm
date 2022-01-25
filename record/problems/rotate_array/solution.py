class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        
        def reversing(i, j):
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i, j = i+1, j-1
        
        k = k % len(nums)
        # reverse all
        reversing(0, len(nums)-1)
        
        # reverse first k
        reversing(0, k - 1)
        
        # reverse remaining
        reversing(k, len(nums)-1)
            
        