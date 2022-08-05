class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
    
        cache = defaultdict(int)
        def dfs(idx, rem): 
            if rem in cache.keys():
                return cache[rem] 
            if rem < 0:
                return 0
            if rem == 0:
                return 1
            for i in range( len(nums) ):
                cache[rem] += dfs(i, rem - nums[i])
            return cache[rem]

        return dfs(0, target)
                