class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backTrack(start, acc):
            ans.append(acc.copy())
            for i in range(start, n):
                acc.append(nums[i])
                backTrack(i + 1, acc)
                acc.pop()
        n = len(nums)
        ans = []
        backTrack(0, [])
        return ans
