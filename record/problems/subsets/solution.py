class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backTrack(idx, acc):
            if idx >= n:
                ans.append(acc.copy())
                return
            
            # decision to include nums[i]
            acc.append(nums[idx])
            backTrack(idx+1, acc)
            
            # decision to exclude nums[i]
            acc.pop()
            backTrack(idx+1, acc)
 
        n = len(nums)
        ans = []
        backTrack(0, [])
        return ans
 