class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        def dfs(i, acc):
            if i >= n:
                res.append(acc.copy())
                return
            # add nums[i]
            acc.append(nums[i])
            dfs(i+1, acc)
            
            # not add nums[i]
            acc.pop() 
            while i + 1 < n and nums[i+1] == nums[i]:  #right branch don't include number in left branch
                i += 1
            dfs(i+1, acc)
            
        nums.sort()
        n = len(nums)
        res = [] 
        dfs(0, [])
        return res
    