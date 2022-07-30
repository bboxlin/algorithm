class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        counter = Counter(nums)
        def dfs(acc):
            if len(acc) == n:
                res.append(acc.copy())
                return 
            for num in counter.keys():
                if counter[num] > 0:
                    acc.append(num)
                    counter[num] -= 1
                    
                    dfs(acc)
                    
                    acc.pop()
                    counter[num] += 1
        n = len(nums)
        res = []
        dfs([])
        return res                    