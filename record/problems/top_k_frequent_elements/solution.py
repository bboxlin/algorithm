class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        memo = {}
        for n in nums:
            if n in memo:
                memo[n] += 1
            else:
                memo[n] = 1
                
        lst = list(memo.items())
        lst.sort(key = lambda x:x[1], reverse= True)
        res = []
        for i in range(k):
            res.append(lst[i][0])
            
        return res
            
                
            
            