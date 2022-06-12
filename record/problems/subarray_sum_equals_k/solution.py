class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        freq = collections.defaultdict(int)
        freq[0] = 1
        cursum = 0 
        res = 0 
        
        for n in nums:
            cursum += n 
            if cursum - k in freq.keys():
                res += freq[cursum - k]
            freq[cursum] += 1
        return res
    
