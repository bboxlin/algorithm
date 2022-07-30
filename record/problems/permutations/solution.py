class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # res = []
        # def dfs(acc):
        #     if len(acc) == len(nums):
        #         res.append(acc.copy())
        #     for num in nums:
        #         if num in set(acc): continue
        #         acc.append(num)
        #         dfs(acc)
        #         acc.pop()                   
        # dfs([])
        # return res
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