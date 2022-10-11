class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        minv = medv = math.inf 
        for val in nums:
            if val <= minv:
                minv = val 
            elif val <= medv:
                medv = val 
            else:
                return True
        return False