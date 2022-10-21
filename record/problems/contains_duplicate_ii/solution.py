class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        val2idx = {} 
        for i, num in enumerate(nums):
            if num in val2idx and abs(val2idx[num]- i) <= k:
                return True
            val2idx[num] = i
        return False
                