class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        n = len(nums)
        visited = set()
        for i in range(n):
            if i + 1 < n:
                cursum = nums[i] + nums[i+1]
                if cursum in visited:
                    return True 
                visited.add(cursum)
        return False