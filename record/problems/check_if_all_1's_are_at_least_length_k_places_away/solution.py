class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        prev = -math.inf
        for i, num in enumerate(nums):
            if num == 1 and prev+k >= i:
                return False 
            if num == 1:
                prev = i
        return True 
