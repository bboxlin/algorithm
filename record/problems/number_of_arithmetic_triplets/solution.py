class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        
        def helper(i):
            lres = 0
            rres = 0
            for l in range(i):
                if nums[l] == nums[i] - diff:
                    lres += 1
            
            for r in range(n-1, i, -1):
                if nums[r] == nums[i] + diff:
                    rres += 1

            return min(lres, rres)
        
        ans = 0
        n = len(nums)
        for i in range(n):
            ans += helper(i)
        
        return ans
            
            