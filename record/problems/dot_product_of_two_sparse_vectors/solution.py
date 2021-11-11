from functools import reduce 
class SparseVector:
    def __init__(self, nums: List[int]):
        self.vector = nums
        
    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        return reduce(lambda x,y: x+y, map(lambda v1,v2: v1*v2, self.vector, vec.vector))

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)